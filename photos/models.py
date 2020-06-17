# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    account = models.OneToOneField(User)
    name = models.CharField(max_length=50)
    photo = models.ImageField()

