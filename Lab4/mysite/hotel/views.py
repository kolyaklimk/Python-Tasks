from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Reservation, TypeRoom, Room, Payment, Client, Period, Reservation
from django.shortcuts import get_object_or_404


# Create
def create_type_room(name):
    type_room = TypeRoom(name=name)
    type_room.save()
    return type_room


def create_room(type_id, capacity, price, description, photo):
    type_room = get_object_or_404(TypeRoom, id=type_id)
    room = Room(type=type_room, capacity=capacity, price=price, description=description, photo=photo)
    room.save()
    return room


def create_payment(new_type):
    payment = Payment(type=new_type)
    payment.save()
    return payment


def create_client(last_name, name, patronymic, commentary, has_child, payment_types):
    client = Client(last_name=last_name, name=name, patronymic=patronymic, commentary=commentary, has_child=has_child)
    client.save()
    client.payment_type.set(payment_types)
    return client


def create_period(check_in_date, eviction_date):
    period = Period(check_in_date=check_in_date, eviction_date=eviction_date)
    period.save()
    return period


def create_reservation(client_id, room_id, check_in_date, eviction_date):
    client = get_object_or_404(Client, id=client_id)
    room = get_object_or_404(Room, id=room_id)
    period = create_period(check_in_date, eviction_date)
    reservation = Reservation(client=client, room=room, residence_period=period)
    reservation.save()
    return reservation


# Read
def get_type_room(type_id):
    return get_object_or_404(TypeRoom, id=type_id)


def get_room(room_id):
    return get_object_or_404(Room, id=room_id)


def get_payment(payment_id):
    return get_object_or_404(Payment, id=payment_id)


def get_client(client_id):
    return get_object_or_404(Client, id=client_id)


def get_period(period_id):
    return get_object_or_404(Period, id=period_id)


def get_reservation(reservation_id):
    return get_object_or_404(Reservation, id=reservation_id)


# Update
def update_type_room(type_id, name):
    type_room = get_object_or_404(TypeRoom, id=type_id)
    type_room.name = name
    type_room.save()
    return type_room


def update_room(room_id, type_id, capacity, price, description, photo):
    room = get_object_or_404(Room, id=room_id)
    type_room = get_object_or_404(TypeRoom, id=type_id)
    room.type = type_room
    room.capacity = capacity
    room.price = price
    room.description = description
    room.photo = photo
    room.save()
    return room


def update_payment(payment_id, new_type):
    payment = get_object_or_404(Payment, id=payment_id)
    payment.type = new_type
    payment.save()
    return payment


def update_client(client_id, last_name, name, patronymic, commentary, has_child, payment_types):
    client = get_object_or_404(Client, id=client_id)
    client.last_name = last_name
    client.name = name
    client.patronymic = patronymic
    client.commentary = commentary
    client.has_child = has_child
    client.payment_type.set(payment_types)
    client.save()
    return client


def update_period(period_id, check_in_date, eviction_date):
    period = get_object_or_404(Period, id=period_id)
    period.check_in_date = check_in_date
    period.eviction_date = eviction_date
    period.save()
    return period


# Delete
def delete_type_room(type_id):
    type_room = get_object_or_404(TypeRoom, id=type_id)
    type_room.delete()


def delete_room(room_id):
    room = get_object_or_404(Room, id=room_id)
    room.delete()


def delete_payment(payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    payment.delete()


def delete_client(client_id):
    client = get_object_or_404(Client, id=client_id)
    client.delete()


def delete_period(period_id):
    period = get_object_or_404(Period, id=period_id)
    period.delete()


def delete_reservation(reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    reservation.delete()
