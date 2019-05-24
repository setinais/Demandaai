from django.urls import path
from . import views

urlpatterns = [
    path('home-adm', views.home, name='home-adm')
]
