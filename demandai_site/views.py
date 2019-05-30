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
        'profissionais': Profile.objects.filter(role='SE').count(),
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
            'estatistica': {
                'demanda': Demand.objects.filter(action='SER', action_id=preparar_dados.id, status='S').count(),
                'analise': Demand.objects.filter(action='SER', action_id=preparar_dados.id,status='E').count(),
                'finalizada': Demand.objects.filter(action='SER', action_id=preparar_dados.id,status='F').count(),
            },
            'institution': {
                'nome': preparar_dados.institution.nome,
                'local': preparar_dados.institution.city,
                'email': preparar_dados.institution.email
            },
            'user': {
                'nome': preparar_dados.profile.first_name,
                'email': preparar_dados.profile.email
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
            'estatistica': {
                'demanda': Demand.objects.filter(action='LAB', action_id=preparar_dados.id, status='S').count(),
                'analise': Demand.objects.filter(action='LAB', action_id=preparar_dados.id, status='E').count(),
                'finalizada': Demand.objects.filter(action='LAB', action_id=preparar_dados.id, status='F').count(),
            },
            'institution': {
                'nome': preparar_dados.institution.nome,
                'local': preparar_dados.institution.city,
                'email': preparar_dados.institution.email
            },
            'user': {
                'nome': preparar_dados.profile.first_name,
                'email': preparar_dados.profile.email
            }
        }
    elif action == 'equ':
        preparar_dados = Equipment.objects.get(pk=id)
        template = 'site/about_portifolio/equipment.html'
        dados = {
            'id': preparar_dados.id,
            'nome': preparar_dados.nome,
            'descricao': preparar_dados.descricao,
            'estatistica': {
                'demanda': Demand.objects.filter(action='EQU', action_id=preparar_dados.id, status='S').count(),
                'analise': Demand.objects.filter(action='EQU', action_id=preparar_dados.id, status='E').count(),
                'finalizada': Demand.objects.filter(action='EQU', action_id=preparar_dados.id, status='F').count(),
            },
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
                'nome': preparar_dados.profile.first_name,
                'email': preparar_dados.profile.email
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
def demandDetail(request, email, codigo):
    demandas = Demand.objects.filter(email=email, codigo=codigo)
    demanda = demandas[0]
    action = {}
    if demanda.action == 'SER':
        action = Service.objects.get(id=demanda.action_id)
    elif demanda.action == 'LAB':
        action = Laboratory.objects.get(id=demanda.action_id)
    elif demanda.action == 'EQU':
        action = Equipment.objects.get(id=demanda.action_id)
    else:
        return HttpResponseNotFound('<h1>Erro Interno 500</h1>')

    dados = {
        'demanda': demanda,
        'action': action
    }
    return render(request, 'site/visualizar_demanda.html', {'dados': dados})


def login_in(request):
    if request.method == 'GET':
        return render(request, 'site/login.html')
    email = request.POST['email']
    password = request.POST['password']
    profile = authenticate(request, username=email, password=password)
    if profile is not None:
        login(request, profile)
        return redirect('home-adm')
    else:
        return render(request, 'site/login.html', {'error': 'Email/Senha Incorretos!'})

def search(request, text):
    lista_servicos = []
    i = 0

    s_inicio = Service.objects.filter(nome__contains=text)
    l_inicio = Laboratory.objects.filter(nome__contains=text)
    e_inicio = Equipment.objects.filter(nome__contains=text)
    s_des = Service.objects.filter(descricao__contains=text)
    l_des = Laboratory.objects.filter(descricao__contains=text)
    e_des = Equipment.objects.filter(descricao__contains=text)

    i_s = 0
    if len(s_inicio) > len(s_des):
        i_s = len(s_inicio)
    else:
        i_s = len(s_des)

    while i < i_s:
        if len(s_inicio) > i:
            if len(s_des) > i:
                if s_inicio[i].id == s_des[i].id:
                    prepare = {
                        'id': s_inicio[i].id,
                        'nome': s_inicio[i].nome,
                        'descricao': s_inicio[i].descricao
                    }
                    lista_servicos.append(prepare)
                else:
                    prepare = {
                        'id': s_inicio[i].id,
                        'nome': s_inicio[i].nome,
                        'descricao': s_inicio[i].descricao
                    }
                    prepare2 = {
                        'id': s_des[i].id,
                        'nome': s_des[i].nome,
                        'descricao': s_des[i].descricao
                    }
                    lista_servicos.append(prepare)
                    lista_servicos.append(prepare2)
            else:
                prepare = {
                    'id': s_inicio[i].id,
                    'nome': s_inicio[i].nome,
                    'descricao': s_inicio[i].descricao
                }
                lista_servicos.append(prepare)
        elif len(s_des) > i:
            prepare = {
                'id': s_des[i].id,
                'nome': s_des[i].nome,
                'descricao': s_des[i].descricao
            }
            lista_servicos.append(prepare)
        # elif s_des is None:
        i += 1
    i = 0

    dados = {
        'lista_servicos': lista_servicos
    }
    return render(request, 'site/search.html', {'dados': dados})