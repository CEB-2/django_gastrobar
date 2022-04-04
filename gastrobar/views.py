from django.shortcuts import render
from django.http import HttpResponse
from gastrobar.forms import ReservationForm
from gastrobar.models import Reservation, Dish
import random
from datetime import datetime
def main(request):
	carta = Dish.objects.all()
	context = {
		'carta' : carta,
	}
	return render(request, 'carta.html', context)

def menu(request):
	dish = Dish.objects.all()
    # seed values
	first = calc_menu(1,3)
	second = calc_menu(4,6)
	dessert = calc_menu(7,9)
    # dish values
	dish_first = Dish.objects.get(pk=first)
	dish_second =Dish.objects.get(pk=second) 
	dish_dessert =Dish.objects.get(pk=dessert) 
	context = {
		'dish_first' :  dish_first, 
	    'dish_second':  dish_second, 
        'dish_dessert': dish_dessert,
    }
    # pasar primary key de los platos
	return render(request, 'menu.html', context)

def carta(request):
	cartaFirst = Dish.objects.all().filter(type="1")
	cartaSecond = Dish.objects.all().filter(type="2")
	cartaThird = Dish.objects.all().filter(type="3")
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

def calc_menu(val1, val2):
    random.seed(datetime.today().strftime("gY-&m-%d"))
    return random. randint(val1, val2)

def map(request):
	return render(request, 'map.html')
