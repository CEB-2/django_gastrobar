from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def legal(request):
	return render(request, 'legal.html')

def privacy(request):
	return render(request, 'privacy.html')