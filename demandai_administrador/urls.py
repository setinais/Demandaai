from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-adm'),
    path('prospeccao', views.prospeccao, name='prospeccao'),
    path('encaminhar-demanda/<str:action>/<int:id>', views.encaminhar_demanda, name='encaminhar-demanda'),
    path('eda', views.encaminhar_demanda_acao, name='encaminhar-d-action'),
    path('rejeitar-demanda', views.rejeitar_demanda, name='rejeitar-demanda'),
]
