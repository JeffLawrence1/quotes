# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-27 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0004_auto_20170927_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='quotes',
            field=models.ManyToManyField(related_name='_user_quotes_+', to='login_app.User'),
        ),
    ]
