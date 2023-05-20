from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<marquee><h1>we are python developers</h1></marquee')
def mouni(request):
    return HttpResponse('<b> i am python student</b>')


