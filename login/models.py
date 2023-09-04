from django.db import models
from schtools.models import Cart, Schedule

class User(models.Model):
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)

# known bug: google input may be large than model size
class Student(User):
    studentID = models.CharField(max_length=200)
    major = models.CharField(max_length=200)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    schedules = models.ManyToManyField(Schedule)

class Advisor(User):
    schedules = models.ManyToManyField(Schedule, blank=True)
    students = models.ManyToManyField(Student)
