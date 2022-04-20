from django.shortcuts import render
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
	first = int(calc_menu(10,12))
	second = int(calc_menu(13,15))
	dessert = int(calc_menu(16,18))
    # dish values
	dish_first = Dish.objects.filter(pk=first)
	dish_second = Dish.objects.filter(pk=second)
	dish_dessert = Dish.objects.filter(pk=dessert)
	first_dish = float(dish_first[0].price.replace(',','.'))
	second_dish = float(dish_second[0].price.replace(',','.'))
	third_dish = float(dish_dessert[0].price.replace(',','.'))
	dish_price = (first_dish + second_dish + third_dish) * 0.8
	format_dish_price = round(dish_price, 2)
	context = {
		'dish_first' :  dish_first, 
	    'dish_second':  dish_second, 
        'dish_dessert': dish_dessert,
		'dish_price' : dish_price,
		'format_dish_price' : format_dish_price,
		
	
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

def homeGB(request):
	return render(request, 'homeGB.html')

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
