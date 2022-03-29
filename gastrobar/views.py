from django.shortcuts import render
from django.http import HttpResponse
from gastrobar.forms import ReservationForm
from gastrobar.models import Reservation, Dish

<<<<<<< HEAD

def main(request):
	
	return render(request, 'main.html')
=======
def home(request):
    return render(request, 'main.html')
>>>>>>> 2cceb6daf1410f524f7495d8f2160c2ead440d1d

def bar(request):
	gastrobar = gastrobar.objects.all()
	context = {
		'gastrobar' : gastrobar,
        
	}

	return render(request, 'menu.html', context)

def dish(request):
	dish = Dish.objects.all()

	return render(request, 'plato.html')

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
