from __future__ import unicode_literals
from django.db import models
import re, bcrypt


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['fname']) < 2 or not postData['fname'].isalpha():
            errors['fname'] = "The first name cannot be empty and should be longer than 2 characters and must be a letter"
        if len(postData['lname']) < 2 or not postData['lname'].isalpha():
            errors['lname'] = "The last name cannot be empty should be longer than 2 characters and must be a letter"
        potential_matches = User.objects.filter(email=postData['email'])
        if len(potential_matches) > 0:
            errors['unique_email'] = "This email already exists"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Please enter a valid email"
        if len(postData['pwd']) < 8:
            errors['pwd'] = "Password should be atleast 8 characters long"
        if postData['pwd'] != postData['pwd1']:
            errors['pwds'] = "Passwords do not match"
        return errors


    def loginvalidator(self, postData):
        errors = {}
        if len(postData['email']) < 1:
            errors['no_email'] = "Please input an email."
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Please enter a valid email"
        elif not User.objects.get(email=postData['email']):
            errors['unique_email'] = "This email is not registered in our database."
        if len(postData['pwd']) < 1:
            errors['no_pass'] = "Please input a password."
        elif len(postData['pwd']) < 3:
            errors['short_pass'] = "Incorrect password: less than 8 characters."
        elif bcrypt.checkpw(postData['pwd'].encode(), User.objects.get(email=postData['email']).password.encode()) == False:
            errors['incorrect_pass'] = "Incorrect password: does not match password stored in database."
        return errors



class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
