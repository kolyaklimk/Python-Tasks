from django.shortcuts import render, get_object_or_404, redirect

from hotel.models import Room, Booking


# Create your views here.
def get_book(request):
    all_booking = Booking.objects.filter(client_id=request.user)
    return render(request, 'profile_user/profile.html', {'all_booking': all_booking})


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return get_book(request)
