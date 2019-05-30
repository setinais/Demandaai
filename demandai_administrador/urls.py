from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-adm'),
    path('prospeccao', views.prospeccao, name='prospeccao'),
]
