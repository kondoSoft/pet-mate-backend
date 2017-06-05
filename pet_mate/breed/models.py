# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Breed(models.Model):
    language = models.CharField(max_length=2, model_index=True)
    name = models.CharField(max_length=250)
    description = models.TextField()
    thumbnail = models.ImageField() 
