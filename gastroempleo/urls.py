from django.urls import path
from gastroempleo import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/offer', views.offer, name='offer'),
]