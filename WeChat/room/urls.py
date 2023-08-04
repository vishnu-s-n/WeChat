from django.urls import path

from .import views

urlpatterns=[
    path('',views.ChatRooms, name='rooms'),
    path('<slug:slug>', views.ChatRoom, name='room')
]