from django.shortcuts import render
from django.http import HttpResponse
from gastrobar.forms import ReservationForm
from gastrobar.models import Reservation, Dish

def home(request):
<<<<<<< HEAD
    return render(request, 'main.html')
# Create your views here.
=======
	
	return render(request, 'main.html')
>>>>>>> 8191abaa8b346af017af397adc671765612113e2

def bar(request):
	gastrobar = gastrobar.objects.all()
	context = {
		'gastrobar' : gastrobar,
        
	}

	return render(request, 'bar.html', context)

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
