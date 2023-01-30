from django.shortcuts import render
#request handler
#return html content to the client

from django.http import HttpResponse
from django.template import loader

def say_hello(request):
    template = loader.get_template('hello.html')
    context={
        'test':'test'
    }
    return HttpResponse(template.render(context,request))
