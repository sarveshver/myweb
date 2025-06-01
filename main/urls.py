from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.addproject, name='addproject'),

     path('send-about-me/', views.send_about_me, name='send_about_me'),
   
]
