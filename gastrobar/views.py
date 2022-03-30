from django.shortcuts import render
from django.http import HttpResponse
from gastrobar.forms import ReservationForm
from gastrobar.models import Reservation, Dish

def main(request):
	carta = Dish.objects.all()
	context = {
		'carta' : carta,
        
	}
	return render(request, 'carta.html', context)

def menu(request):
	menu = menu.objects.all()
	context = {
		'menu' : menu,
        
	}

	return render(request, 'menu.html', context)

def carta(request):
	carta = Dish.objects.all()
	
	context = {
		'carta' : carta,
        
	}
	return render(request, 'carta.html', context)

def dish(request):
	dish = Dish.objects.all()
	
	context = {
		'dish' : dish,
        
	}
	return render(request, 'dish.html', context)


def reservation(request):
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

	