from django.urls import path 
from . import views

#URLconf
urlpatterns=[
    path('landpage/',views.say_hello)
]