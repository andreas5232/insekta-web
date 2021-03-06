# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-24 17:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scenarios', '0008_auto_20160123_0223'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScenarioGroupEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(default=1)),
                ('scenario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scenarios.Scenario')),
            ],
        ),
        migrations.AddField(
            model_name='scenariogroup',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='scenariogroupentry',
            name='scenario_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scenarios.ScenarioGroup'),
        ),
    ]
