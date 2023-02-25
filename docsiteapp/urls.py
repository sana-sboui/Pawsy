from django.urls import path 
from . import views

#URLconf
urlpatterns=[
    path("klinik/",views.say_hello),
    path("klinik/team.html/", views.team, name="team"),
    path("klinik/about.html/", views.about, name="about"),
    path("klinik/appointment.html/", views.appointment, name="appointment"),
    path("klinik/contact.html/", views.contact, name="contact"),
    path("klinik/feature.html/", views.feature, name="feature"),
    path("klinik/service.html/", views.service, name="service"),
    path("klinik/testimonial.html/", views.testimonial, name="testimonial"),
    
]