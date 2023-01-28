from django.urls import path 
from . import views

#URLconf
urlpatterns=[
    path('index/',views.say_hello)
]