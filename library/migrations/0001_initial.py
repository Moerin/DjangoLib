# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-14 23:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('file_path', models.FileField(upload_to='here')),
            ],
        ),
    ]
