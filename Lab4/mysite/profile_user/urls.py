from . import views
from django.urls import path

app_name = 'profile_user'

urlpatterns = [
    path('', views.get_book, name='profile'),
    path('<int:booking_id>', views.delete_booking, name='delete_booking'),
]
