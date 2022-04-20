from django.shortcuts import render

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
			new = Contacto()

			new.name = form.cleaned_data["name"]
			new.mail = form.cleaned_data["mail"]
			new.asunto = form.cleaned_data["asunto"]
			new.mensaje = form.cleaned_data["mensaje"]


			

	context = {
		'contacto' : contacto,
        'form' : form,
		'value' : value,
    }

	return render(request, 'contacto.html', context)