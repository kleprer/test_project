from django.shortcuts import render
from django.http import HttpResponse


def poll(request):
    return HttpResponse("Hello, poll. .")

def index(request):
    return HttpResponse("Hello, index .")

