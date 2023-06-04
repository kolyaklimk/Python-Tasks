from django.shortcuts import render, redirect
from .models import Room, Client, Booking
from django.shortcuts import get_object_or_404


def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'hotel/hotel_list.html', {'rooms': rooms})


def sort_rooms_by_price(request):
    rooms = Room.objects.order_by('price')
    return render(request, 'hotel/hotel_list.html', {'rooms': rooms, 'is_sort_by_price': True})


def room_detail(request, room_id):
    form = get_object_or_404(Room, id=room_id)
    return render(request, 'room_form.html', {'form': form})

# def create_room(request):
#     form = RoomForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('room_list')
#     return render(request, 'room_form.html', {'form': form})
#
#
# def update_room(request, room_id):
#     room = Room.objects.get(id=room_id)
#     form = RoomForm(request.POST or None, instance=room)
#     if form.is_valid():
#         form.save()
#         return redirect('room_list')
#     return render(request, 'room_form.html', {'form': form})
#
#
# def delete_room(request, room_id):
#     product = Room.objects.get(id=id)
#     product.delete()
