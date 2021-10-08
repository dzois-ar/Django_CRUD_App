from django.db import models


# create database
class Trainer(models.Model):
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length= 100)
    object = models.CharField(max_length= 50)
    description = models.TextField(max_length=500, blank=True)
