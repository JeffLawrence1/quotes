# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0003_quote_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='author',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='quote',
            name='message',
            field=models.CharField(max_length=311),
        ),
    ]
