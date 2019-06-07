from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-adm'),
    path('prospeccao', views.prospeccao, name='prospeccao'),
    path('encaminhar-demanda/<str:action>/<int:id>/', views.encaminhar_demanda, name='encaminhar-demanda'),
]
