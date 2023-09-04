from django.urls import path

from dm import views

app_name = 'dm'

urlpatterns = [
    path('chat/', views.index, name='index'),
    path('chat/<str:username>/', views.chat_page, name='chat_page'),
]