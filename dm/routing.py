from django.urls import path

from dm import consumers

websocket_urlpatterns = [
    path('wss/chat/<int:id>/', consumers.ChatConsumer.as_asgi()),
    
]
