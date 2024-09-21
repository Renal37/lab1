from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def main_page(request:HttpRequest) ->HttpResponse:
    return render(request,'index.html')