from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    title = models.CharField(max_length=5, null=True, blank=True)
    firstName = models.CharField(max_length=200, null=False)
    lastName = models.CharField(max_length=200, null=False)
    email = models.EmailField()
    description = models.TextField()
    