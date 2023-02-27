from django.shortcuts import render
#request handler
#return html content to the client

from django.http import HttpResponse
from django.template import loader

def say_hello(request):
    template = loader.get_template('klinik.html')
    context={
        'test':'test'
    }
    return HttpResponse(template.render(context,request))
def team(request):
    return render(request,"team.html")
def about(request):
    return render(request,"about.html")
def appointment(request):
    return render(request,"appointment.html")
def contact(request):
    return render(request,"contact.html")
def klinik(request):
    return render(request,"klinik.html")
def service(request):
    return render(request,"service.html")
def testimonial(request):
    return render(request,"testimonial.html")
def feature(request):
    return render(request,"feature.html")