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
	cartaFirst = Dish.objects.all().filter(type="first")
	cartaSecond = Dish.objects.all().filter(type="second")
	cartaThird = Dish.objects.all().filter(type="dessert")
	

	

	context = {
		'cartaFirst' : cartaFirst,
		'cartaSecond' : cartaSecond,
		'cartaThird' : cartaThird,
		
		
        
	}
	return render(request, 'carta.html', context)

def dish(request, pk):
	dish = Dish.objects.get(pk=pk)
	
	context = {
		'dish' : dish,
        
	}
	return render(request, 'plato.html', context)


def reservation(request):
	form = ReservationForm()
	value = False
	if request.method == "POST":
		form = ReservationForm(request.POST)
		if form.is_valid():
			value = True
			new = Reservation()

			new.name = form.cleaned_data["name"]
			new.mail = form.cleaned_data["mail"]
			new.phone = form.cleaned_data["phone"]
			new.date = form.cleaned_data["date"]
			new.time = form.cleaned_data["time"]
			new.count_p = form.cleaned_data["count_p"]
			new.save()


	context = {
		'reservation' : reservation,
        'form' : form,
		'value' : value,
		
    }

	return render(request, 'reservation.html', context)


