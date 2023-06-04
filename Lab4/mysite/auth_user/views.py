from django.contrib.auth import logout
from datetime import date
from django.shortcuts import redirect
from django import forms


def logout_user(request):
    logout(request)
    return redirect('hotel:hotel_list')


def validate_age(value: date):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 18:
        raise forms.ValidationError("You must be 18 years or older.")
