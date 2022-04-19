from django.urls import path
from gastroempleo import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>', views.offer, name='offer'),
]