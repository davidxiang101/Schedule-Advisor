# login/urls.py
from django.urls import path
from .views import user_redirect
from . import views
import django.http


urlpatterns = [
path('', views.user_redirect, name="user_redirect"),
path('login/profile/', views.profile_view, name="profile"),
path('login/profile/edit', views.profile_edit_view, name="edit_profile"),
path('login/profile/save', views.submit_edits_view, name="save_edits"),

]