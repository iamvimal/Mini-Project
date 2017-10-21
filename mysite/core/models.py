from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Restaurant(models.Model):
    rest_id = models.IntegerField(primary_key=True)
    rest_name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    rating = models.IntegerField(default=0)

    def __unicode__(self):
        return self.rest_name

class FoodMenu(models.Model):
    menu_id = models.IntegerField(primary_key=True)
    food_name = models.CharField(max_length=20)
    food_type = models.CharField(max_length=20)
    rest_id = models.ForeignKey(Restaurant)
    cost = models.IntegerField(default=0)

    def __unicode__(self):
        return self.food_name

class UserCart(models.Model):
    username = models.ForeignKey(User)
    menu_id = models.ForeignKey(FoodMenu)

    def __unicode__(self):
        return '{} {}'.format(self.username, self.menu_id)

class UserAddress(models.Model):
    username = models.ForeignKey(User)
    door_no = models.IntegerField(default=0)
    street = models.CharField(max_length=15)
    locality = models.CharField(max_length=15)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.IntegerField(default=0)

    def __unique__(self):
        return '{} {} {}'.format(self.username, self.door_no, self.street, self.locality, self.city, self.state, self.zipcode)

