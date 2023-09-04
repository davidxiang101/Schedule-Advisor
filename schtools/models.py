from django.db import models
from search.models import Class

class Cart(models.Model):
    classes = models.ManyToManyField(Class)

class Schedule(models.Model):
    name = models.CharField(max_length=200, default='Schedule')
    studentFirstName = models.CharField(max_length=200, default='')
    studentLastName = models.CharField(max_length=200, default='')
    classes = models.ManyToManyField(Class)
    approved = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)