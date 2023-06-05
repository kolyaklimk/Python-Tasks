from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Room, Category, Booking
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.utils import timezone
import calendar
import requests


def timezone_context(request):
    quote = ''
    joke = ''
    if request.user.is_authenticated:
        url = 'http://api.forismatic.com/api/1.0/'
        params = {
            'method': 'getQuote',
            'format': 'json',
            'lang': 'en'
        }
        response = requests.get(url, params=params)

        url = "https://icanhazdadjoke.com/"
        headers = {"Accept": "application/json"}
        response_joke = requests.get(url, headers=headers)

        try:
            if response.status_code == 200 or response_joke.status_code == 200:
                data = response.json()
                quote = (data['quoteText'])
                joke = response_joke.json()['joke']
            else:
                quote = ('Ошибка при выполнении запроса:', response.status_code)
                joke = ('Ошибка при выполнении запроса:', response.status_code)
        except:
            quote = 'No internet connection'
            joke = 'No internet connection'

    user_timezone = timezone.get_current_timezone()
    current_date = timezone.now()
    c = calendar.HTMLCalendar(calendar.MONDAY).formatmonth(datetime.now().year, datetime.now().month)
    context = {
        'user_timezone': user_timezone,
        'current_date': current_date,
        'calendar': c,
        'quote': quote,
        'joke': joke,
    }
    return context


def room_list(request, category_id):
    def get_html():
        if category_id == 0:
            rooms = Room.objects.all()
        else:
            rooms = Room.objects.filter(category_id=category_id)

        categories = Category.objects.all()
        return render(request, 'hotel/hotel_list.html', {'rooms': rooms,
                                                         'categories': categories,
                                                         'choose_category': category_id,
                                                         'timezone_context': timezone_context(request)})

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
                                                     'choose_category': category_id,
                                                     'timezone_context': timezone_context(request)})


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
        if check_in_date >= check_out_date:
            error_message = "Check in date <= Check out date!"
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
        return redirect("profile_user:profile")

    if request.method == 'POST' and 'edit_room' in request.POST:
        price = request.POST['price']
        capacity = request.POST['capacity']
        select = request.POST['select']
        photo = request.POST['photo']

        category = get_object_or_404(Category, id=select)
        form.category = category
        form.capacity = capacity
        form.price = price
        form.photo = photo

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
        photo = request.POST['photo']

        category = get_object_or_404(Category, id=select)

        new_room = Room()
        new_room.category = category
        new_room.photo = photo
        new_room.capacity = capacity
        new_room.price = price
        new_room.save()
        return redirect("hotel:hotel_list", 0)

    return render(request, 'hotel/room_create.html', {'categories': categories})


def analyse(request):
    if not request.user.is_authenticated:
        return redirect("hotel:hotel_list", 0)

    bookings = Booking.objects.all()
    list_total_cost = [booking.calculate_total_cost() for booking in bookings]
    sum_cost = sum(list_total_cost)
    average_bill = sum_cost / len(list_total_cost)

    popular_rooms = Booking.objects.values('room').annotate(total_bookings=Count('room')). \
        order_by('-total_bookings').first()
    total_bookings = popular_rooms['total_bookings']
    room = Room.objects.get(id=popular_rooms['room'])

    return render(request, 'hotel/hotel_analyse.html', {'bookings': bookings,
                                                        'total_earnings': sum_cost,
                                                        'average_bill': average_bill,
                                                        'total_bookings': total_bookings,
                                                        'most_popular_room': room})
