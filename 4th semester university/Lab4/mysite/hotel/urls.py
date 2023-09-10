from . import views
from django.urls import path

app_name = 'hotel'

urlpatterns = [
    path('sort_by/<int:category_id>/', views.room_list, name='hotel_list'),
    path('sort_by/<int:category_id>/sort_by_price/', views.sort_rooms_by_price, name='hotel_list_sort_by_price'),
    path('room/<int:room_id>', views.room_detail, name='room_id'),
    path('add/', views.create_room, name='room_create'),
    path('analyse/', views.analyse, name='hotel_analyse')
]
