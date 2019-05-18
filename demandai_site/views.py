from inspect import getmembers
from pprint import pprint
from random import *

from django.forms import ModelForm
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from demandai_administrador.models import Laboratory, Equipment, Service, User, Demand


# Create your views here.
def start(request, template_name='site/index.html'):

    servicos_id = sample(range(1,50),6)
    dados = {
        'servicos': Service.objects.count(),
        'laboratorios': Laboratory.objects.count(),
        'equipamentos': Equipment.objects.count(),
        'profissionais': User.objects.count(),
        'lista_servicos': Service.objects.filter(pk__in=servicos_id),
        'lista_portifolio': {
            'servicos': Service.objects.filter(pk__in=[1,2,3]),
            'laboratorios': Laboratory.objects.filter(pk__in=[1,2,3]),
            'equipamentos': Equipment.objects.filter(pk__in=[1,2,3]),
            },
        }
    return render(request, template_name, {'dados': dados})

def about_portifolio(request, action, id):

    dados = {}
    template = ''

    if action == 'ser':
        preparar_dados = Service.objects.get(pk=id)
        template = 'site/about_portifolio/service.html'
        dados = {
            'nome': preparar_dados.nome,
            'descricao': preparar_dados.descricao,
            'plataformas': preparar_dados.plataformas,
            'institution': {
                'nome': preparar_dados.institution.nome,
                'local': preparar_dados.institution.city,
                'email': preparar_dados.institution.email
            },
            'user': {
                'nome': preparar_dados.user.nome,
                'email': preparar_dados.user.email
            }
        }
    elif action == 'lab':
        preparar_dados = Laboratory.objects.get(pk=id)
        template = 'site/about_portifolio/laboratory.html'
        dados = {
            'nome': preparar_dados.nome,
            'descricao': preparar_dados.descricao,
            'atividade_realizadas': preparar_dados.atividades_realizadas,
            'pesext': preparar_dados.pesquisa_extensao,
            'institution': {
                'nome': preparar_dados.institution.nome,
                'local': preparar_dados.institution.city,
                'email': preparar_dados.institution.email
            },
            'user': {
                'nome': preparar_dados.user.nome,
                'email': preparar_dados.user.email
            }
        }
    elif action == 'equ':
        preparar_dados = Equipment.objects.get(pk=id)
        template = 'site/about_portifolio/equipment.html'
        dados = {
            'nome': preparar_dados.nome,
            'descricao': preparar_dados.descricao,
            'laboratory': {
                'nome': preparar_dados.laboratory.nome,
                'id': preparar_dados.laboratory.id,
            },
            'institution': {
                'nome': preparar_dados.institution.nome,
                'local': preparar_dados.institution.city,
                'email': preparar_dados.institution.email
            },
            'user': {
                'nome': preparar_dados.user.nome,
                'email': preparar_dados.user.email
            }
        }
    else:
        return HttpResponseNotFound('<h1>Pagina não encontrada</h1>')
    return render(request, template, {'dados': dados})

class DemandForm(ModelForm):
    class Meta:
        model = Demand
        fields = ['nome', 'cpf', 'data_nascimento', 'email', 'telefone', 'descricao', 'action', 'action_id']

def demandarSelected(request, action, id):

    dados = {
        'ser': Service.objects.all(),
        'lab': Laboratory.objects.all(),
        'equ': Equipment.objects.all(),
        'action': action,
        'action_id': id,
        'errors': request.body
    }
    return render(request, 'site/demandar.html/', {'dados': dados})

def demandar(request):
    dados = {
        'ser': Service.objects.all(),
        'lab': Laboratory.objects.all(),
        'equ': Equipment.objects.all(),
    }
    return render(request, 'site/demandar.html/', {'dados': dados})

def createDemand(request):
    form = DemandForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('demandar', {'dados': {'message': 'Cadastradp cp, sucesso'}})
    else:
        pprint(getmembers(form.errors))
        old = form.errors
        return redirect('demandar/'+request.body.action+'/'+request.body.action_id)