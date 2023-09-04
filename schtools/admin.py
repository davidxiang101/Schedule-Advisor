from django.contrib import admin

# Register your models here.
from .models import Cart, Schedule
admin.site.register(Cart)
admin.site.register(Schedule)