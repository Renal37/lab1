from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def contacts_page(request:HttpRequest) ->HttpResponse:
    return render(request,'contacts.html')
