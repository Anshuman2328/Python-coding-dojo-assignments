from __future__ import unicode_literals
from django.db import models
import re, bcrypt
from datetime import datetime
from ..app_one.models import *

# Create your models here.



class ItemManager(models.Manager):
    def item_validator(self, postData):
        errors = {}
        if len(postData['item']) < 2:
            errors['itemlength'] = "More than 2 characters."

        return errors

class Item(models.Model):
    item = models.CharField(max_length = 255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    item_created = models.ForeignKey(User, related_name = "user_created", on_delete='models.CASCADE')
    item_add = models.ManyToManyField(User, related_name="item_by_users")
    objects = ItemManager()
