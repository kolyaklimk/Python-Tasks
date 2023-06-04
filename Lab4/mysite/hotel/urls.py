from . import views
from django.urls import path

app_name = 'hotel'

urlpatterns = [
    path('', views.room_list, name='hotel_list'),
    path('sort_by_price/', views.sort_rooms_by_price, name='hotel_list_sort_by_price'),
    path('<int:id>', views.room_detail),
    # path('edit/<int:id>/', views.product_edit),
    # path('delete/<int:id>/', views.product_delete),
    # path('create/', views.product_create),
]
