from django.shortcuts import render
from django.core.mail import send_mail

from django_gastrobar.forms import ContactoForm


def send_user_mail(name, mail, asunto, contenido):
	
		send_mail(
		'Usuario: '+ name,
		'Mail de usuario: ' + mail + "\n" + "Asunto: " + asunto + "\n" + "Contenido: " + contenido ,
		'djangogastrobb@gmail.com',
		['danelibiza@gmail.com'],
		fail_silently=False,
		)

def home(request):
	return render(request, 'home.html')

def legal(request):
	return render(request, 'legal.html')

def privacy(request):
	return render(request, 'privacy.html') 

def contacto(request):
	form = ContactoForm()
	value = False
	if request.method == "POST":
		form = ContactoForm(request.POST)
		if form.is_valid():
			value = True

			name = form.cleaned_data["name"]
			mail = form.cleaned_data["mail"]
			asunto = form.cleaned_data["asunto"]
			mensaje = form.cleaned_data["mensaje"]
			send_user_mail(name, mail, asunto, mensaje)

			

	context = {
		'contacto' : contacto,
        'form' : form,
		'value' : value,
    }

	return render(request, 'contacto.html', context)

	