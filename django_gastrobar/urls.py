"""django_gastrobar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django_gastrobar import views
from django.urls import path, include
from gastrobar import urls
from gastroblog import urls
from gastroempleo import urls


urlpatterns = [
    path('', views.home, name='home'),
    path('gastrobar/', include('gastrobar.urls')),
    path('gastroblog/', include('gastroblog.urls')),
    path('gastroempleo/', include('gastroempleo.urls')),
    path('legalAdvice/',views.legal, name='legal'),
    path('privacy/',views.privacy, name='privacy'),
    path('gastrobar/contacto/',views.contacto, name='contacto'),
    path('gastroblog/contacto/',views.contacto, name='contacto'),
]
