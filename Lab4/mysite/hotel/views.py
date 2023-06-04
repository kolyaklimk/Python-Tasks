from django.shortcuts import render, redirect
from .models import Room, Client, Booking, Category
from django.shortcuts import get_object_or_404


def room_list(request, category_id):
    if category_id == 0:
        rooms = Room.objects.all()
    else:
        rooms = Room.objects.filter(category_id=category_id)

    categories = Category.objects.all()
    return render(request, 'hotel/hotel_list.html', {'rooms': rooms,
                                                     'categories': categories,
                                                     'choose_category': category_id})


def sort_rooms_by_price(request, category_id):
    if category_id == 0:
        rooms = Room.objects.order_by('price')
    else:
        rooms = Room.objects.filter(category_id=category_id).order_by('price')

    categories = Category.objects.all()
    return render(request, 'hotel/hotel_list.html', {'rooms': rooms,
                                                     'is_sort_by_price': True,
                                                     'categories': categories,
                                                     'choose_category': category_id})


def room_detail(request, room_id):
    form = get_object_or_404(Room, id=room_id)
    return render(request, 'hotel/room_detail.html', {'form': form})

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
