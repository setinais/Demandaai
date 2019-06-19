from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-adm'),
    path('prospeccao', views.prospeccao, name='prospeccao'),
    path('prospeccao/encaminhar-demanda/<str:action>/<int:id>', views.encaminhar_demanda, name='encaminhar-demanda'),
    path('prospeccao/eda', views.encaminhar_demanda_acao, name='encaminhar-d-action'),
    path('prospeccao/rejeitar-demanda', views.rejeitar_demanda, name='rejeitar-demanda'),
    path('prospeccao/detalhes-demanda/<int:id>', views.detalhes_demanda, name='detalhes-demanda'),
    path('prospeccao/download_arquivos', views.download_arquivos, name='download_arquivos'),
    path('prospeccao/responder_solicitante', views.responder_solicitante, name='responder_solicitante'),
]
