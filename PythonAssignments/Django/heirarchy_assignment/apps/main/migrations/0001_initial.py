# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 19:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boss_relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='boss_relationship',
            name='boss_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='superior_relationship', to='main.Employee'),
        ),
        migrations.AddField(
            model_name='boss_relationship',
            name='underling_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subordinate_relationship', to='main.Employee'),
        ),
    ]
