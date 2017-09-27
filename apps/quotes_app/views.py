# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..login_app.models import User, Quote
from django.contrib import messages

# Create your views here.

def seshCheck(request):
    try:
        return request.session['user_id']
    except:
        return False

def index(request):
    if seshCheck(request) == False:
        return redirect("/")

    user = User.objects.get(id= request.session["user_id"])
    favorites = user.quotes.all()
    
    

    context = {
        "quotes": Quote.objects.exclude(user_id=request.session['user_id']),
        "favs": favorites,
        # "user": Quote.objects.filter(id=request.session['user_id']),
    }
    return render(request, "quotes_app/home.html", context)

def addquote(request):
    if seshCheck(request) == False:
        return redirect("/")

    results = {"status": True, "errors": []}
    if len(request.POST["author"]) < 4:
        results["errors"].append("Quoted by must be longer than 3 chars")
    if len(request.POST["message"]) < 10:
        results["errors"].append("Message must be longer than 10 chars")
    if len(results["errors"]) > 0:
        results["status"] = False
    if results["status"] == False:
        for error in results["errors"]:
            messages.error(request, error)
        return redirect("/quote")
    else:
        user = User.objects.get(id= request.session["user_id"])
        Quote.objects.create(author=request.POST['author'], message=request.POST['message'], user=user)

        return redirect('/quote')
    
def user(request, user_id):
    if seshCheck(request) == False:
        return redirect("/")


    context = {
        "user": User.objects.filter(id=user_id),
        "qcount": Quote.objects.filter(user=user_id).count(),
        "quotes": Quote.objects.filter(user=user_id)

    }
    return render(request, "quotes_app/landing.html", context)

def addfav(request, pid):
    user = User.objects.get(id= request.session["user_id"])
    newquote = Quote.objects.get(id = pid)
    user.quotes.add(newquote.id)
    return redirect('/quote')

def remove(request, pid):
    user = User.objects.get(id= request.session["user_id"])
    badquote = Quote.objects.get(id = pid)
    user.quotes.remove(badquote.id)
    return redirect('/quote')