from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='home'),

    # Ver detalhes do item selecionado no portifolio
    path('about-portifolio/<str:action>/<int:id>', views.about_portifolio, name='about_portifolio'),

    # Cadastrar nova demanda vindo de um portifolio
    path('demandar/<str:action>/<int:id>', views.demandarSelected, name='demanda_selecionada'),

    # Cadastrar nova demanda
    path('demandar', views.demandar, name='demandar'),

    # Ver detalhes da demanda
    path('demand/detail/<str:email>/<str:codigo>', views.demandDetail, name='demand_detail'),

    # Login
    path('login', views.login_in, name='login'),

    # Consulta de relações
    path('search', views.search, name='search'),
    #path('search?text=<str:text>', views.search, name='search_val'),
]
