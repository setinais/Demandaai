from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home-adm'),
    path('logout', views.logout_in, name='logout'),

    # Administrativo
        # Prospecção
        path('prospeccao', views.prospeccao, name='prospeccao'),
        path('prospeccao/encaminhar-demanda/<str:action>/<int:id>', views.encaminhar_demanda, name='encaminhar-demanda'),
        path('prospeccao/eda', views.encaminhar_demanda_acao, name='encaminhar-d-action'),
        path('prospeccao/rejeitar-demanda', views.rejeitar_demanda, name='rejeitar-demanda'),
        path('prospeccao/detalhes-demanda/<int:id>', views.detalhes_demanda, name='detalhes-demanda'),
        path('prospeccao/download_arquivos', views.download_arquivos, name='download_arquivos'),
        path('prospeccao/responder_solicitante', views.responder_solicitante, name='responder_solicitante'),

        # Serviços
        path('service',views.servicos,name='service'),
        path('service/cadastro',views.servicos_cadastro,name='service.cadastro'),
        path('service/editar/<int:id>',views.servicos_editar,name='service.editar'),
        path('service/deletar/<int:id>',views.servicos_deletar,name='service.deletar'),
        path('service/receber/<int:id>',views.servicos_receber,name='service.receber'),
        path('service/cancelar/<int:id>',views.servicos_cancelar,name='service.cancelar'),

        # Equipamentos
        path('equipament', views.equipamentos, name='equipament'),
        path('equipament/cadastro', views.equipamentos_cadastro, name='equipament.cadastro'),
        path('equipament/editar/<int:id>', views.equipamentos_editar, name='equipament.editar'),
        path('equipament/deletar/<int:id>', views.equipamentos_deletar, name='equipament.deletar'),

        # Laboratorios
        path('laboratory', views.laboratorios, name='laboratory'),
        path('laboratory/cadastro', views.laboratorios_cadastro, name='laboratory.cadastro'),
        path('laboratory/editar/<int:id>', views.laboratorios_editar, name='laboratory.editar'),
        path('laboratory/deletar/<int:id>', views.laboratorios_deletar, name='laboratory.deletar'),

        # Controle de Acesso
        path('permission/<int:id>', views.permission, name='permission'),
        path('permission_edit/<int:id>', views.permission_edit, name='permission.edit'),
        path('permession/solicitacao',views.permission_solicitacao,name='permission.solicitacao'),


        # Profile
        path('profile',views.profile,name='profile'),
        # path('profile/cadastro',views.profile_cadastro,name='profile.cadastro'),
        path('profile/editar',views.profile_editar,name='profile.editar'),
        path('profile/deletar/<int:id>',views.profile_deletar,name='profile.deletar'),
        path('profile/desativar',views.profile_desativar,name='profile.desativar'),

        # Instituições
        path('institution', views.institution, name='institution'),
        path('institution/cadastro', views.institution_cadastro, name='institution.cadastro'),
        path('institution/editar/<int:id>', views.institution_editar, name='institution.editar'),
        path('institution/deletar/<int:id>', views.institution_deletar, name='institution.deletar'),

        # Notificação
        path('notificacao/<int:id>', views.notificacao, name='notificacao'),

    # Users
        # Demanda
        path('demand', views.demand, name='demand'),
        path('demand_ar/<str:ar>/<int:id>', views.demand_ar, name='demand_ar')
]