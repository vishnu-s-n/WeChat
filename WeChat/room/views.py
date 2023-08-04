from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room,Message

@login_required
def ChatRooms(request):
    rooms = Room.objects.all()

    return render(request, 'rooms.html', {'rooms' : rooms})

@login_required
def ChatRoom(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room = room)[0:25]


    return render(request, 'room.html', {'room' : room, 'messages' : messages})

