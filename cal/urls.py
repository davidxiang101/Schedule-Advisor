# cal/urls.py
from django.urls import path
from . import views
import django.http


urlpatterns = [
path('cal/', views.cal_view, name="cal"),
path('cal/display/<int:id>/', views.display_view, name="display"),
]
