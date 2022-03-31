from django.urls import path
from gastrobar import views

urlpatterns = [
    path('', views.carta, name='carta'),
    path('menu', views.menu, name='menu_dia'),
    path('carta', views.carta, name='carta'),
    path('dish/<int:pk>/', views.dish, name='dish'),
    #path('<int:pk>/', views.dish, name='dish'),
    path('reservation', views.reservation, name='reservation'),


    
    
]
