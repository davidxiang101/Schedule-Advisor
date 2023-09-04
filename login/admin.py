from django.contrib import admin

# Register your models here.

from .models import User, Student, Advisor
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Advisor)