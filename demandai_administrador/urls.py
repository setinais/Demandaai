from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home-adm'),
    path('logout', views.logout_in, name='logout'),

    # Prospecção
    path('prospeccao', views.prospeccao, name='prospeccao'),
    path('prospeccao/encaminhar-demanda/<str:action>/<int:id>', views.encaminhar_demanda, name='encaminhar-demanda'),
    path('prospeccao/eda', views.encaminhar_demanda_acao, name='encaminhar-d-action'),
    path('prospeccao/rejeitar-demanda', views.rejeitar_demanda, name='rejeitar-demanda'),
    path('prospeccao/detalhes-demanda/<int:id>', views.detalhes_demanda, name='detalhes-demanda'),
    path('prospeccao/download_arquivos', views.download_arquivos, name='download_arquivos'),
    path('prospeccao/responder_solicitante', views.responder_solicitante, name='responder_solicitante'),

    # Serviços
    path('service',views.servicos,name='servicos'),
    path('service/cadastro',views.servicos_cadastro,name='servicos.cadastro'),
    path('service/editar/<int:id>',views.servicos_editar,name='servicos.editar'),
    path('service/deletar/<int:id>',views.servicos_deletar,name='servicos.deletar'),

    # Equipamentos
    path('equipament', views.equipamentos, name='equipamentos'),
    path('equipament/cadastro', views.equipamentos_cadastro, name='equipamentos.cadastro'),
    path('equipament/editar/<int:id>', views.equipamentos_editar, name='equipamentos.editar'),
    path('equipament/deletar/<int:id>', views.equipamentos_deletar, name='equipamentos.deletar'),

    # Laboratorios
    path('laboratory', views.laboratorios, name='laboratorios'),
    path('laboratory/cadastro', views.laboratorios_cadastro, name='laboratorios.cadastro'),
    path('laboratory/editar/<int:id>', views.laboratorios_editar, name='laboratorios.editar'),
    path('laboratory/deletar/<int:id>', views.laboratorios_deletar, name='laboratorios.deletar'),
]
