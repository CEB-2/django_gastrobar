from django.urls import path
from gastrobar import views


urlpatterns = [
<<<<<<< HEAD
    path('', views.main, name='main'),
    path('bar', views.bar, name='menu'),
=======
    path('', views.home, name='home'),
    path('bar', views.bar, name='menubar'),
>>>>>>> 2cceb6daf1410f524f7495d8f2160c2ead440d1d
    path('dish', views.dish, name='dish'),
    path('reservation', views.reservation, name='reservation'),

]