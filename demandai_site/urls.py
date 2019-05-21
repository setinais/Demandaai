from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='home'),
    path('about-portifolio/<str:action>/<int:id>', views.about_portifolio, name='about_portifolio'),
    path('demandar/<str:action>/<int:id>', views.demandarSelected, name='demanda_selecionada'),
    path('demandar', views.demandar, name='demandar'),

]