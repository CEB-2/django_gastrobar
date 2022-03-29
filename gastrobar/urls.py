from django.urls import path
from gastrobar import views


urlpatterns = [
    path('', views.home, name='home'),
    path('bar', views.bar, name='menubar'),
    path('dish', views.dish, name='dish'),
    path('reservation', views.reservation, name='reservation'),

]