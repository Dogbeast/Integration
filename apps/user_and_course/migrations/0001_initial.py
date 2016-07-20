# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 20:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_and_registration', '0002_auto_20160719_1050'),
    ]

    operations = [
        migrations.CreateModel(
            name='users_in_courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=50)),
                ('num_users', models.IntegerField()),
                ('User_in_Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_and_registration.Users')),
            ],
            managers=[
                ('userManager', django.db.models.manager.Manager()),
            ],
        ),
    ]