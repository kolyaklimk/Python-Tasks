from django.shortcuts import render, get_object_or_404, redirect

from hotel.models import Room, Booking


# Create your views here.
def get_book(request):
    if not request.user.is_authenticated:
        return redirect("hotel:hotel_list", 0)

    def get_booking():
        return Booking.objects.filter(client_id=request.user, status='cart')

    if request.method == 'POST' and 'delete_item' in request.POST:
        booking = get_object_or_404(Booking, id=request.POST['booking_id'])
        booking.delete()
        return render(request, 'profile_user/profile.html', {'all_booking': get_booking()})

    if request.method == 'POST' and 'confirm' in request.POST:
        for i in Booking.objects.filter(client_id=request.user, status='cart'):
            i.status = 'paid'
            i.save()
        return render(request, 'profile_user/profile.html', {'all_booking': get_booking()})

    return render(request, 'profile_user/profile.html', {'all_booking': get_booking()})
