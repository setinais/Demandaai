import binascii
import os
from random import *
from django.contrib.auth import authenticate, login


import _thread
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect

from demandai_administrador.models import Laboratory, Equipment, Service
from .forms import *
from django.views.decorators.http import require_http_methods

# Create your views here.
def start(request, template_name='site/index.html'):

    servicos_id = sample(range(1,50),6)
    dados = {
        'servicos': Service.objects.count(),
        'laboratorios': Laboratory.objects.count(),
        'equipamentos': Equipment.objects.count(),
        'profissionais': Profile.objects.count(),
        'lista_servicos': Service.objects.filter(pk__in=servicos_id),
        'lista_portifolio': {
            'servicos': Service.objects.filter(pk__in=[1,2,3]),
            'laboratorios': Laboratory.objects.filter(pk__in=[1,2,3]),
            'equipamentos': Equipment.objects.filter(pk__in=[1,2,3]),
            },
        }
    return render(request, template_name, {'dados': dados, 'user': request.user.is_authenticated})

def about_portifolio(request, action, id):

    dados = {}
    template = ''

    if action == 'ser':
        preparar_dados = Service.objects.get(pk=id)
        template = 'site/about_portifolio/service.html'
        dados = {
            'id': preparar_dados.id,
            'nome': preparar_dados.nome,
            'descricao': preparar_dados.descricao,
            'plataformas': preparar_dados.plataformas,
            'institution': {
                'nome': preparar_dados.institution.nome,
                'local': preparar_dados.institution.city,
                'email': preparar_dados.institution.email
            },
            'user': {
                'nome': preparar_dados.user.first_name,
                'email': preparar_dados.user.email
            }
        }
    elif action == 'lab':
        preparar_dados = Laboratory.objects.get(pk=id)
        template = 'site/about_portifolio/laboratory.html'
        dados = {
            'id': preparar_dados.id,
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
                'nome': preparar_dados.user.first_name,
                'email': preparar_dados.user.email
            }
        }
    elif action == 'equ':
        preparar_dados = Equipment.objects.get(pk=id)
        template = 'site/about_portifolio/equipment.html'
        dados = {
            'id': preparar_dados.id,
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
                'nome': preparar_dados.user.first_name,
                'email': preparar_dados.user.email
            }
        }
    else:
        return HttpResponseNotFound('<h1>Pagina não encontrada</h1>')
    return render(request, template, {'dados': dados})

def demandarSelected(request, action, id):
    dados = {
        'ser': Service.objects.all(),
        'lab': Laboratory.objects.all(),
        'equ': Equipment.objects.all(),
        'action': action,
        'action_id': id,
        'errors': request.body
    }

    if request.method == 'GET':
        form = DemandForm()
        return render(request, 'site/demandar.html', {'dados': dados, 'form': form})
    else:
        HttpResponseNotFound('<h1>Error 404 Not Found</h1>')

def demandar(request):
    dados = {
        'ser': Service.objects.all(),
        'lab': Laboratory.objects.all(),
        'equ': Equipment.objects.all(),
    }
    if request.method == 'GET':
        form = DemandForm()
        return render(request, 'site/demandar.html', {'dados': dados, 'form': form})
    else:
        post = request.POST.copy()
        post['codigo'] = binascii.hexlify(os.urandom(3)).decode().upper()
        form = DemandForm(post)
        if form.is_valid():
            form.save()
            _thread.start_new_thread(form.send_mail, (request,))
            form = DemandForm()
            return render(request, 'site/demandar.html',{'dados': dados,'form': form, 'message': post['codigo']})
        return render(request, 'site/demandar.html', {'dados': dados, 'form': form})


@require_http_methods(["GET"])
def demandDetail(request, cpf, codigo):
    return HttpResponse({'descrição: aqui deve ser implementado o detalhe da demanda'})


def login_in(request):
    if request.method == 'GET':
        return render(request, 'site/login.html')
    email = request.POST['email']
    password = request.POST['password']
    profile = authenticate(request, username=email, password=password)
    if profile is not None:
        if hasattr(request.POST, 'conection_permanent'):
            login(request, profile)
        return redirect('home-adm')
    else:
        return render(request, 'site/login.html', {'error': 'Email/Senha Incorretos!'})

