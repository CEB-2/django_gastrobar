from django.shortcuts import render
from django.http import HttpResponse
from gastroempleo.models import Empleo

def home(request):
    empleos = Empleo.objects.all()
    context = {
		'empleos' : empleos,
	}

    return render(request, 'homeGE.html', context)


def offer(request, pk):
    empleo = Empleo.objects.get(pk=pk)
	
    context = {
		'empleo' : empleo,
	}
    return render(request, 'offer.html', context) 
