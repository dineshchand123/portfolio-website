from django.contrib import admin
from django.urls import path
from personal import views

urlpatterns = [
     path("", views.index, name='home'),
     path("about", views.about, name='about'),
     path("resume", views.resume, name='resume'),
     path("portfolio", views.portfolio, name='portfolio'),
    path("services", views.services, name='services'), 
    path("contact", views.contact, name='contact'),
]