from django.urls import path
from gastrobar import views


urlpatterns = [
    path('', views.main, name='main'),
    path('bar', views.bar, name='menu'),
    path('dish', views.dish, name='dish'),
    path('reservation', views.reservation, name='reservation'),

]