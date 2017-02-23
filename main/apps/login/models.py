from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
# Create your models here.
class UserManager(models.Manager):
    def validate_User(self, post_data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        error_msgs = []
        print post_data
        if EMAIL_REGEX.match(post_data['e-mail']):
            print 'Hit Submit!'
            print post_data
        else:
            error_msgs.append('invalid e-mail')

        if (len(post_data['password'])<8):
            error_msgs = ('invalid password')

        elif (post_data['password'] != post_data['pwconfirm']):
            error_msgs = ('passwords do not match')

        else:
            password = post_data['password'].encode()
            hashed = bcrypt.hashpw(password, bcrypt.gensalt())

        if (len(post_data['first_name'])<2):
            error_msgs = ('first name is too short')


        if (len(post_data['last_name'])<2):
            error_msgs = ('last name is too short')

        if error_msgs:
            return {
            'errors': error_msgs
            }
        else:
            validated_user = User.objects.create(first_name=post_data['first_name'], last_name=post_data['last_name'],email=post_data['e-mail'],password=hashed, pwconfirm=post_data['pwconfirm'] )
            return {
            'the_user': validated_user
            }
class User(models.Model):
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=75)
    pwconfirm = models.CharField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
