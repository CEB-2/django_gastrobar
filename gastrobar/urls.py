from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.bar, name='bar'),
    path('', views.dish, name='dish'),
    #path('<int:pk>/', views.reservation, name='book'),
    path('', views.reservation, name='reservation'),
    
]
