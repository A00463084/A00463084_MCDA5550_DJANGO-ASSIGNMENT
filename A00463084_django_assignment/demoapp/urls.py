from django.urls import path
from . import views

urlpatterns= [
    path("home/", views.home, name="home"),
    path("hotel_list/", views.Hotels_list, name="hotelList"),
    path("hotel_list/<str:pk>", views.Hotels_detail, name="hotelDetail"),
]