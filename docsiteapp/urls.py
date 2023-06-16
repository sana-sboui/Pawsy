from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static
from quizzz import views as quizzz_views


#URLconf
urlpatterns=[
    path('klinik/klinik.html',views.klinik,name='klinik'),
    path('klinik/about.html',views.about,name='about'),
    path('klinik/feature.html',views.feature,name='feature'),
    path('klinik/team.html',views.team,name='team'),
    path('klinik/service.html',views.service,name='service'),
    path('klinik/appointment.html',views.appointment,name='appointment'),
    path('klinik/contact.html',views.contact,name='contact'),
    path('klinik/testimonial.html',views.testimonial,name='testimonial'),   
    path('klinik/vet.html',views.vet ,name='vet'),
    path("signup/", views.signup_login, name="signup"),
    path("login/", views.signup_login, name="login"),
    path('', views.signup_login, name='signup_login'),
    path('logout/', views.logout_view, name='logout'),
    path('klinik/appointments.html',views.appointment_list,name='doctor'),
    path('klinik/adopter.html', views.adopter, name='adopter'),
    path('klinik/accept-appointment/<int:appointment_id>/', views.accept_appointment, name='accept_appointment'),  
    path('klinik/cancel-appointment/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
    path('klinik/quizzes',quizzz_views.quiz_list,name='quiz_list'),
    path('klinik/quizzes/<str:quiz_name>', quizzz_views.quiz_detail, name='quiz_detail'),
    path('api/v1/quizzes/<str:quiz_name>', quizzz_views.quiz_data, name='quiz_data'),

] 