# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodMenu',
            fields=[
                ('menu_id', models.IntegerField(serialize=False, primary_key=True)),
                ('food_name', models.CharField(max_length=20)),
                ('food_type', models.CharField(max_length=20)),
                ('cost', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('rest_id', models.IntegerField(serialize=False, primary_key=True)),
                ('rest_name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('door_no', models.IntegerField(default=0)),
                ('street', models.CharField(max_length=15)),
                ('locality', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zipcode', models.IntegerField(default=0)),
                ('username', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserCart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('menu_id', models.ForeignKey(to='core.FoodMenu')),
                ('username', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='foodmenu',
            name='rest_id',
            field=models.ForeignKey(to='core.Restaurant'),
        ),
    ]
