from django.shortcuts import render
#request handler
#return html content to the client

from django.http import HttpResponse

def say_hello(request):
    return render(request,"hello.html")
