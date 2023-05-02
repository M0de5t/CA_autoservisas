from django.urls import path
from . import views



urlpatterns = [
    # index
    path('', views.index, name="index"),
    # displays all cars
    path("cars/", views.cars, name= 'cars'),
    # display car
    path('<int:car_id>', views.specific_car, name='specific_car'),
    # display services
    path('services/', views.services, name='services'),
    # all order
    path('orders/', views.orders, name='orders'),
    # specific order
    path('orders/<int:order_id>',views.specific_orders, name='specific_order')
]
