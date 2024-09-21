from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def about_page(request:HttpRequest) -> HttpResponse:
    return render(request, 'about.html')
