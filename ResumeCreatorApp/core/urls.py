from . import views
from django.urls import path
urlpatterns = [
    path('home.html/', views.home),
    path('service.html/', views.service),
    path('skill.html/', views.skill),
    path('contact.html/', views.contact),
    path('data.html/', views.Data),
    path('info.html/', views.info),

]