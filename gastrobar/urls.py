from django.urls import path
from gastrobar import views

urlpatterns = [
    path('', views.carta, name='carta'),
    path('menu', views.menu, name='menu'),
    path('carta', views.carta, name='carta'),
    path('<int:pk>', views.dish, name='dish'),
    path('reservation', views.reservation, name='reservation'),
    path('map', views.map, name='map'), 
]
