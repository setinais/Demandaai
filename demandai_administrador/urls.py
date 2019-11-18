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
    path('servicos',views.servicos,name='servicos'),
    path('servicos/cadastro',views.servicos_cadastro,name='servicos.cadastro'),
    path('servicos/editar/<int:id>',views.servicos_editar,name='servicos.editar'),
    path('servicos/deletar/<int:id>',views.servicos_deletar,name='servicos.deletar'),
    path('equipamentos', views.equipamentos, name='equipamentos'),
    path('equipamentos/cadastro', views.equipamentos_cadastro, name='equipamentos.cadastro'),
    path('equipamentos/editar/<int:id>', views.equipamentos_editar, name='equipamentos.editar'),
    path('equipamentos/deletar/<int:id>', views.equipamentos_deletar, name='equipamentos.deletar'),
]
