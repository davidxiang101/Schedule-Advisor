# search/urls.py
from django.urls import path
from . import views
import django.http


urlpatterns = [
path('search/', views.search_view, name="search"),
path('search/class', views.search_class_view, name="class_search"),
path('search/add', views.search_add_view, name="add_search"),
]
