# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 18:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_lecturer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='lecturer',
        ),
    ]