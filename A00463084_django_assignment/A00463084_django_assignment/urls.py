"""A00463084_django_assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

# NOTE: All the URLS ARE ADDED UNDER THE DEMO APP URLS.PY FILE

urlpatterns= [
    path('admin/', admin.site.urls),
    url(r'^',include('demoapp.urls'))
]

'''
path("home/", views.home, name="home"),
    path("hotel_list/", views.Hotels_list, name="hotelList"),
    path("hotel_list/<str:pk>", views.Hotels_detail, name="hotelDetail"),
    path("generics_hotel_list/", views.get_generics_list.as_view(), name="genericsList"),
    path("guest_list/", views.guest_list)
'''
