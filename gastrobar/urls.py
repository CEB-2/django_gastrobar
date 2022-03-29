from django.urls import path
from gastrobar import views


urlpatterns = [
    path('', views.home, name='home'),
<<<<<<< HEAD
    #path('', TemplateView().as_view(template_name='main.html')),
    #path('', views.bar, name='bar'),
    path('dish', views.dish, name='dish'),
    #path('<int:pk>/', views.reservation, name='book'),
    #path('', views.reservation, name='reservation'),  
=======
    path('bar', views.bar, name='bar'),
    path('dish', views.dish, name='dish'),
    path('reservation', views.reservation, name='reservation'),
    
>>>>>>> 8191abaa8b346af017af397adc671765612113e2
]
