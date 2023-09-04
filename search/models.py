from django.db import models

# known bug: google input may be large than model size
class Class(models.Model):
    subject = models.CharField(max_length=200)
    catalog_nbr = models.IntegerField()
    descr = models.CharField(max_length=200) 
    days = models.CharField(max_length=200) 
    start_time = models.CharField(max_length=200) 
    end_time = models.CharField(max_length=200) 
    crse_id = models.IntegerField(default=-1)
    class_section = models.IntegerField(default=-1)
