from django.urls import path 
from . import views

#URLconf
urlpatterns=[
    path('klinik/',views.say_hello)
]