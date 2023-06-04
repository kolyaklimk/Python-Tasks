from datetime import datetime

from django.shortcuts import render
from .models import Room, Category, Client, Booking
from django.shortcuts import get_object_or_404
from django import forms


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
    global periods

    def check_date_periods(start1, end1, start2, end2):
        if start1 < end2 and start2 < end1:
            return True
        else:
            return False

    form = get_object_or_404(Room, id=room_id)

    if request.method == 'POST':
        check_in_date = datetime.strptime(request.POST['check_in_date'], '%Y-%m-%d').date()
        check_out_date = datetime.strptime(request.POST['check_out_date'], '%Y-%m-%d').date()
        has_child = request.POST.get('my_checkbox', False)
        if check_in_date > check_out_date:
            error_message = "Check in date < Check out date!"
            return render(request, 'hotel/room_detail.html', {'error_message': error_message})

        periods = []

        all_booking = Booking.objects.filter(room_id=room_id)
        for i in all_booking:
            if check_date_periods(check_in_date, check_out_date, i.check_in_date, i.check_out_date):
                periods.append(str(i.check_in_date) + ' --> ' + str(i.check_out_date))

        if len(periods):
            error_message = "Already booked these days: " + str(periods) + '!'
            return render(request, 'hotel/room_detail.html', {'error_message': error_message})

        booking = Booking(
            room=form,
            client=request.user,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            has_child=True if has_child == "on" else False
        )
        booking.save()
        return room_list(request, 0)

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
