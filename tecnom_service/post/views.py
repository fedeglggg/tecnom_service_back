from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.method == "POST":
        print(request.POST)
        return HttpResponse("posting data")
        
    elif request.method == "GET":
        print(request.GET)
        return HttpResponse("getting data")