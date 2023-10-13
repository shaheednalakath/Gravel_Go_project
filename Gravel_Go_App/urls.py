from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('service/', views.service, name="service"),
    path('packages/', views.packages, name="packages"),
    path('destination/', views.destination, name="destination"),
    path('booking/', views.booking, name="booking"),
    path('travelguid/', views.tavelguid, name="travelguid"),
    path('testimonial/', views.testimonial, name="testimonial"),
    path('error/', views.error, name="error"),
    path('contact/', views.contact, name="contact")

]
