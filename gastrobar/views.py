from django.shortcuts import render
from django.http import HttpResponse
from gastrobar.forms import ReservationForm
from gastrobar.models import Reservation, Dish

def home(request):
    return HttpResponse("hello")
# Create your views here.

def bar(request):
	gastrobar = gastrobar.objects.all()
	context = {
		'gastrobar' : gastrobar,
        
	}

	return render(request, 'home.html', context)

def dish(request):
	dish = Dish.objects.all()
	
	context = {
		'dish' : dish,
        
	}
	return render(request, 'dish.html', context)

def reservation(request, pk):
	reservation = Reservation.objects.get(pk=pk)
	form = ReservationForm()

	if request.method == "POST":
		form = ReservationForm(request.POST)
		if form.is_valid():
			new = Reservation()(
				name=form.cleaned_data["name"],
				mail=form.cleaned_data["mail"],
                phone=form.cleaned_data["phone"],
                date=form.cleaned_data["date"],
                time=form.cleaned_data["time"],
                count_p=form.cleaned_data["count_p"],
			)
			new.save()


	context = {
		'reservation' : reservation,
        'form' : form,
    }

	return render(request, 'reservation.html', context)
