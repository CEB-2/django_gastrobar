from django.shortcuts import render
from django.core.mail import send_mail

from django_gastrobar.forms import ContactoForm

from django.views.generic import TemplateView

def send_user_mail(name, mail, asunto, contenido):
	
		send_mail(
		'Usuario: '+ name,
		'Mail de usuario: ' + mail + "\n" + "Asunto: " + asunto + "\n" + "Contenido: " + contenido ,
		'djangogastrobb@gmail.com',
		['djangogastrobb@gmail.com'],
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

	if "gastroblog" in request.path:
		base_template = "mainBlog.html"
	else:
		base_template = "main.html"

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
		'base_template' : base_template,

    }

	return render(request, 'contacto.html', context)

