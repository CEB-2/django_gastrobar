from django.urls import path
from gastrobar import views


urlpatterns = [
    path('', views.home, name='home'),
<<<<<<< HEAD
    path('bar', views.bar, name='menu'),
=======
    path('bar', views.bar, name='bar'),
>>>>>>> 054dac918c4b05e9403323daf8af7dc6fb99e11e
    path('dish', views.dish, name='dish'),
    path('reservation', views.reservation, name='reservation'),
    
]
