from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
import _thread
from demandai_administrador.models import Demand, Service, Laboratory, Equipment
from .forms import *
from datetime import datetime, timedelta

@login_required
def home(request):
    return render(request, 'administrador/home.html', {'user': request.user.is_authenticated})

@login_required
def prospeccao(request):
    try:
        demandas = Demand.objects.filter(visualizada=0).order_by('-created_at')
        dados = []
        i = 0
        while i < len(demandas):
            action = {}
            demanda = {}
            if demandas[i].action == 'SER':
                action = Service.objects.get(id=demandas[i].action_id)
            elif demandas[i].action == 'LAB':
                action = Laboratory.objects.get(id=demandas[i].action_id)
            elif demandas[i].action == 'EQU':
                action = Equipment.objects.get(id=demandas[i].action_id)
            else:
                return HttpResponseNotFound('<h1>Erro Interno 500</h1>')
            demanda = {
                'id': demandas[i].id,
                'status': demandas[i].get_status_display(),
                'created_at': demandas[i].created_at,
                'visualizada': demandas[i].visualizada,
                'badge': badge_select(demandas[i].status),
                'action': {
                    'nome': action.nome,
                    'profile': {
                        'nome': action.profile.username,
                        'id': action.profile.id
                    },
                    'instituicao': action.institution.nome,
                }
            }
            dados.append(demanda)
            i += 1
        return render(request, 'administrador/prospeccao.html', {'dados': dados})
    except Exception:
        return render(request, 'site/error.html')


def badge_select(val):
    return {
        'S': 'warning',
        'E': 'info',
        'R': 'danger',
        'A': 'primary',
        'P': 'secondary',
        'F': 'success',
    }[val]

@login_required
def encaminhar_demanda(request, action, id):
    try:
        template = ''
        actions = []
        if action == 'SER':
            template = 'administrador/encaminhar_demanda/servico.html'
            actions = Service.objects.filter(status=0)
        elif action == 'LAB':
            template = 'administrador/encaminhar_demanda/laboratorio.html'
            actions = Laboratory.objects.filter(status=0)
        elif action == 'EQU':
            template = 'administrador/encaminhar_demanda/equipamento.html'
            actions = Equipment.objects.filter(status=0)
        else:
            return HttpResponseNotFound('<h1>Erro Interno 500</h1>')

        i=0
        dados = []
        while i < len(actions):
            prepare = {
                'id': actions[i].id,
                'action': action,
                'nome': actions[i].nome,
                'status': actions[i].status,
                'responsavel': actions[i].profile.username,
            }
            dados.append(prepare)
            i += 1
        return render(request, template, {'dados': dados, 'id_demanda': id})
    except Exception:
        return render(request, 'site/error.html')

@login_required
@require_http_methods(["GET"])
def encaminhar_demanda_acao(request):
    try:
        action = {}
        if request.GET['action'] == 'SER':
            action = Service.objects.get(id=request.GET['id'])
        elif request.GET['action'] == 'LAB':
            action = Laboratory.objects.get(id=request.GET['id'])
        elif request.GET['action'] == 'EQU':
            action = Equipment.objects.get(id=request.GET['id'])
        else:
            return render(request, 'site/error.html')
        demanda = Demand.objects.get(id=request.GET['id_demanda'])
        demanda.visualizada = 0
        demanda.status = 'E'
        demanda.save()
        demanda.demand_callback.create(action=request.GET['action'], action_id=request.GET['id'], feedback='Demanda encaminhada para "'+ action.nome+'", ficando em análise!', prazo_feedback=(datetime.today() + timedelta(days=2)))

        _thread.start_new_thread(send_mail, (request,))
        return redirect('prospeccao')
    except Exception:
        return render(request, 'site/error.html')

@login_required
@require_http_methods(["GET"])
def rejeitar_demanda(request):
    try:
        demanda = Demand.objects.get(id=request.GET['id'])
        demanda.status = 'R'
        demanda.save()
        demanda.delete()
        return redirect('prospeccao')
    except Exception:
        return render(request, 'site/error.html')

@login_required
@require_http_methods(['GET'])
def detalhes_demanda(request, id):
    demanda = Demand.objects.get(id=id)
    demand_callback = []
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
        'demanda': {
            'id': demanda.id,
            'action': demanda.action,
            'action_name': demanda.get_action_display(),
            'action_select': '',
            'nome': demanda.nome,
            'email': demanda.email,
            'telefone': demanda.telefone,
            'descricao': demanda.descricao,
            'status': {
                'titulo': demanda.get_status_display(),
                'badge': badge_select(demanda.status)
            },
            'visualizada': demanda.visualizada,
            'created_at': demanda.created_at,
            'updated_at': demanda.updated_at,
            'demand_callbak': demand_callback,
            'tempo_solicitacao': abs((datetime.today() - demanda.created_at).days)
        },
        'time_now': datetime.now()
    }
    return render(request, 'administrador/demanda_detalhes.html', {'dados': dados})