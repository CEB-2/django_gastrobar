from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    #path('', TemplateView().as_view(template_name='main.html')),
    #path('', views.bar, name='bar'),
    path('dish', views.dish, name='dish'),
    #path('<int:pk>/', views.reservation, name='book'),
    #path('', views.reservation, name='reservation'),  
]
