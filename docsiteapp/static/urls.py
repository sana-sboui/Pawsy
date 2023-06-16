from django.urls import path 
from . import views


#URLconf
urlpatterns=[
    path("klinik/klinik.html",views.klinik, name="klinik"),
    path("klinik/team.html", views.team, name="team"),
    path("klinik/about.html", views.about, name="about"),
    path("klinik/appointment.html", views.appointment, name="appointment"),
    path("klinik/contact.html", views.contact, name="contact"),
    path("klinik/feature.html", views.feature, name="feature"),
    path("klinik/service.html", views.service, name="service"),
    path("klinik/testimonial.html", views.testimonial, name="testimonial"),
    path("klinik/vet.html", views.vet, name="vet"), 
    path("signup/", views.signup_login, name="signup"),
    path("login/", views.signup_login, name="login"),
    path('klinik/signup.html', views.signup_login, name='signup_login'),
    path('klinik/appointments.html',views.appointment_list,name='doctor'),
    path('klinik/adopter.html', views.adopter, name='adopter'),
]