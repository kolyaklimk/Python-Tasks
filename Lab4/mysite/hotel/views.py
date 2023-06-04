from datetime import datetime

from django.shortcuts import render, redirect
from .models import Room, Category, Booking
from django.shortcuts import get_object_or_404


def room_list(request, category_id):
    def get_html():
        if category_id == 0:
            rooms = Room.objects.all()
        else:
            rooms = Room.objects.filter(category_id=category_id)

        categories = Category.objects.all()
        return render(request, 'hotel/hotel_list.html', {'rooms': rooms,
                                                         'categories': categories,
                                                         'choose_category': category_id})

    if request.method == 'POST' and 'delete_room' in request.POST:
        room = get_object_or_404(Room, id=request.POST['room_id'])
        room.delete()
        return get_html()

    return get_html()


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
    def check_date_periods(start1, end1, start2, end2):
        if start1 < end2 and start2 < end1:
            return True
        else:
            return False

    form = get_object_or_404(Room, id=room_id)
    categories = Category.objects.all()

    if request.method == 'POST' and 'book_room' in request.POST:
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
        return redirect("hotel:hotel_list", 0)

    if request.method == 'POST' and 'edit_room' in request.POST:
        price = request.POST['price']
        capacity = request.POST['capacity']
        select = request.POST['select']

        category = get_object_or_404(Category, id=select)
        form.category = category
        form.capacity = capacity
        form.price = price

        form.save()
        form = get_object_or_404(Room, id=room_id)

    return render(request, 'hotel/room_detail.html', {'form': form, 'categories': categories})


def create_room(request):
    if not request.user.is_authenticated:
        return redirect("hotel:hotel_list", 0)

    categories = Category.objects.all()
    if request.method == 'POST' and 'create_room' in request.POST:
        price = request.POST['price']
        capacity = request.POST['capacity']
        select = request.POST['select']

        category = get_object_or_404(Category, id=select)

        new_room = Room()
        new_room.category = category
        new_room.photo = '1'
        new_room.capacity = capacity
        new_room.price = price
        new_room.save()
        return redirect("hotel:hotel_list", 0)

    return render(request, 'hotel/room_create.html', {'categories': categories})
