import binascii
import os
from random import *
from django.contrib.auth import authenticate, login

import _thread
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect

from demandai_administrador.models import Laboratory, Equipment, Service, Demandcb, UserService, Notification
from .forms import *
from django.views.decorators.http import require_http_methods
from pprint import pprint

# Create your views here.
def start(request, template_name='site/index.html'):
    try:
        servicos_id = sample(range(1, 50), 6)
        dados = {
            'servicos': Service.objects.count(),
            'laboratorios': Laboratory.objects.count(),
            'equipamentos': Equipment.objects.count(),
            'profissionais': Profile.objects.filter(role='SE').count(),
            'lista_servicos': Service.objects.filter(pk__in=servicos_id),
            'icon': 'fa fa-cogs',
            'lista_portifolio': {
                'servicos': Service.objects.filter(pk__in=[1, 2, 3]),
                'laboratorios': Laboratory.objects.filter(pk__in=[1, 2, 3]),
                'equipamentos': Equipment.objects.filter(pk__in=[1, 2, 3]),
            },
        }
        return render(request, template_name, {'dados': dados, 'user': request.user.is_authenticated})
    except Exception:
        return render(request, 'site/error.html')

def about_portifolio(request, action, id):
    try:
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
                    'analise': Demand.objects.filter(action='SER', action_id=preparar_dados.id, status='E').count(),
                    'finalizada': Demand.objects.filter(action='SER', action_id=preparar_dados.id, status='F').count(),
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
            return render(request, 'site/error.html')
        return render(request, template, {'dados': dados})
    except Exception:
        return render(request, 'site/error.html')

def demandarSelected(request, action, id):
    try:
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
    except Exception:
        return render(request, 'site/error.html')

def demandar(request):
    #try:
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
            form = DemandForm(post, request.FILES)
            if form.is_valid():
                #form.save()
                if form.data['action'] == 'SER':
                    service = Service.objects.get(id=form.data['action_id'])
                    for us in UserService.objects.filter(service_id=form.data['action_id']):
                        notif = Notification.objects.create(
                            titulo='Uma nova demanada Solcitada.',
                            texto='O serviço:<b>'+service.nome+'<b> foi demandado',
                            icone='fa fa-suitcase',
                            ulr='demand',
                            visualizada=False,
                            profile_id=us.profile.id,
                        )
                _thread.start_new_thread(form.send_mail, (request,))
                form = DemandForm()
                return render(request, 'site/demandar.html', {'dados': dados, 'form': form, 'message': post['codigo']})
            return render(request, 'site/demandar.html', {'dados': dados, 'form': form})
    #except Exception:
        #return render(request, 'site/error.html')

@require_http_methods(["GET"])
def demandDetail(request):
    try:
        demandas = Demand.objects.filter(email=request.GET['email'].strip(), codigo=request.GET['codigo'].strip())
        demanda = demandas[0]
        action = {}
        demand_callback = []
        if demanda.action == 'SER':
            action = Service.objects.get(id=demanda.action_id)
        elif demanda.action == 'LAB':
            action = Laboratory.objects.get(id=demanda.action_id)
        elif demanda.action == 'EQU':
            action = Equipment.objects.get(id=demanda.action_id)
        else:
            return render(request, 'site/error.html')
        for callbacks in demanda.demand_callback.order_by('-created_at'):
            action = {}
            if callbacks.action == 'SER':
                action = Service.objects.get(id=callbacks.action_id)
            elif callbacks.action == 'LAB':
                action = Laboratory.objects.get(id=callbacks.action_id)
            elif callbacks.action == 'EQU':
                action = Equipment.objects.get(id=callbacks.action_id)
            demand_callback_dados = {
                'feedback': callbacks.feedback,
                'created_at': callbacks.created_at,
                'action': {
                    'id': action.id,
                    'nome': action.nome,
                    'responsavel': {
                        'nome': action.profile.username,
                        'id': action.profile.id,
                    },
                },
                'id': callbacks.id
            }
            demand_callback.append(demand_callback_dados)
        dados = {
            'demanda': demanda,
            'action': action
        }
        return render(request, 'site/visualizar_demanda.html', {'dados': dados, 'callbacks': demand_callback})
    except Exception:
        return render(request, 'site/error.html')

def login_in(request):
    try:
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
    except Exception:
        return render(request, 'site/error.html')

def search(request):
    try:
        if request.GET['text'] == '':
            return redirect('home')

        lista_servicos = []

        s_inicio = Service.objects.filter(nome__icontains=request.GET['text'])
        l_inicio = Laboratory.objects.filter(nome__icontains=request.GET['text'])
        e_inicio = Equipment.objects.filter(nome__icontains=request.GET['text'])
        s_des = Service.objects.filter(descricao__icontains=request.GET['text'])
        l_des = Laboratory.objects.filter(descricao__icontains=request.GET['text'])
        e_des = Equipment.objects.filter(descricao__icontains=request.GET['text'])
        # return HttpResponse([s_des.count(), s_inicio.count()])
        # pprint(vars(s_inicio))

        i = 0
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
                            'descricao': s_inicio[i].descricao,
                            'icon': 'fa fa-cogs'
                        }
                        lista_servicos.append(prepare)
                    else:
                        prepare = {
                            'id': s_inicio[i].id,
                            'nome': s_inicio[i].nome,
                            'descricao': s_inicio[i].descricao,
                            'icon': 'fa fa-cogs'
                        }
                        prepare2 = {
                            'id': s_des[i].id,
                            'nome': s_des[i].nome,
                            'descricao': s_des[i].descricao,
                            'icon': 'fa fa-cogs'
                        }
                        lista_servicos.append(prepare)
                        lista_servicos.append(prepare2)
                else:
                    prepare = {
                        'id': s_inicio[i].id,
                        'nome': s_inicio[i].nome,
                        'descricao': s_inicio[i].descricao,
                        'icon': 'fa fa-cogs'
                    }
                    lista_servicos.append(prepare)
            elif len(s_des) > i:
                prepare = {
                    'id': s_des[i].id,
                    'nome': s_des[i].nome,
                    'descricao': s_des[i].descricao,
                    'icon': 'fa fa-cogs'
                }
                lista_servicos.append(prepare)
            # elif s_des is None:
            i += 1

        i = 0
        i_s = 0
        if len(l_inicio) > len(l_des):
            i_s = len(l_inicio)
        else:
            i_s = len(l_des)

        while i < i_s:
            if len(l_inicio) > i:
                if len(l_des) > i:
                    if l_inicio[i].id == l_des[i].id:
                        prepare = {
                            'id': l_inicio[i].id,
                            'nome': l_inicio[i].nome,
                            'descricao': l_inicio[i].descricao,
                            'icon': 'ti-desktop'
                        }
                        lista_servicos.append(prepare)
                    else:
                        prepare = {
                            'id': l_inicio[i].id,
                            'nome': l_inicio[i].nome,
                            'descricao': l_inicio[i].descricao,
                            'icon': 'ti-desktop'
                        }
                        prepare2 = {
                            'id': l_des[i].id,
                            'nome': l_des[i].nome,
                            'descricao': l_des[i].descricao,
                            'icon': 'ti-desktop'
                        }
                        lista_servicos.append(prepare)
                        lista_servicos.append(prepare2)
                else:
                    prepare = {
                        'id': l_inicio[i].id,
                        'nome': l_inicio[i].nome,
                        'descricao': l_inicio[i].descricao,
                        'icon': 'ti-desktop'
                    }
                    lista_servicos.append(prepare)
            elif len(l_des) > i:
                prepare = {
                    'id': l_des[i].id,
                    'nome': l_des[i].nome,
                    'descricao': l_des[i].descricao,
                    'icon': 'ti-desktop'
                }
                lista_servicos.append(prepare)
            # elif s_des is None:
            i += 1

        i = 0
        i_s = 0
        if len(e_inicio) > len(e_des):
            i_s = len(e_inicio)
        else:
            i_s = len(e_des)

        while i < i_s:
            if len(e_inicio) > i:
                if len(e_des) > i:
                    if e_inicio[i].id == e_des[i].id:
                        prepare = {
                            'id': e_inicio[i].id,
                            'nome': e_inicio[i].nome,
                            'descricao': e_inicio[i].descricao,
                            'icon': 'fa fa-cog'
                        }
                        lista_servicos.append(prepare)
                    else:
                        prepare = {
                            'id': e_inicio[i].id,
                            'nome': e_inicio[i].nome,
                            'descricao': e_inicio[i].descricao,
                            'icon': 'fa fa-cog'
                        }
                        prepare2 = {
                            'id': e_des[i].id,
                            'nome': e_des[i].nome,
                            'descricao': e_des[i].descricao,
                            'icon': 'fa fa-cog'
                        }
                        lista_servicos.append(prepare)
                        lista_servicos.append(prepare2)
                else:
                    prepare = {
                        'id': e_inicio[i].id,
                        'nome': e_inicio[i].nome,
                        'descricao': e_inicio[i].descricao,
                        'icon': 'fa fa-cog'
                    }
                    lista_servicos.append(prepare)
            elif len(e_des) > i:
                prepare = {
                    'id': e_des[i].id,
                    'nome': e_des[i].nome,
                    'descricao': e_des[i].descricao,
                    'icon': 'fa fa-cog'
                }
                lista_servicos.append(prepare)
            # elif s_des is None:
            i += 1
        dados = {
            'icon': '',
            'lista_servicos': lista_servicos,
            'text': request.GET['text']
        }
        return render(request, 'site/search.html', {'dados': dados})
    except Exception:
        return render(request, 'site/error.html')

