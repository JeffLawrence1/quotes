from django.conf.urls import url, include
from django.contrib import admin
from . import views

# def test(request):
#     print "quotes app urls"

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^$', test),
    url(r'^$', views.index),
    url(r'^addquote$', views.addquote),
    url(r'^user/(?P<user_id>\d+)$', views.user),
    url(r'^addfav/(?P<pid>\d+)$', views.addfav),
    url(r'^remove/(?P<pid>\d+)$', views.remove),
]
