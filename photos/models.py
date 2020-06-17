# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    account = models.OneToOneField(User)
    name = models.CharField(max_length=50)
    photo = models.ImageField()







class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    __unicode__ = lambda self: self.name


class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('Author', related_name='articles', on_delete=models.CASCADE)

    __unicode__ = lambda self: self.title
