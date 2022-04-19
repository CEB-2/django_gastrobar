from django.shortcuts import render
from django.http import HttpResponse

def offer(request):
    return render(request, 'offer.html') 

def home(request):
    return render(request, 'homeGE.html')