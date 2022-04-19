from django.urls import path, include
from gastroempleo import views
from gastrobar import urls
from gastroblog import urls
from gastroempleo import urls

urlpatterns = [

    path('', views.home, name='home'),
]