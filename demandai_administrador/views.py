from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
import _thread
from demandai_administrador.models import Demand, Service, Laboratory, Equipment
from .forms import *

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
        demanda = Demand.objects.get(id=request.GET['id_demanda'])
        demanda.action_id = request.GET['id']
        demanda.action = request.GET['action']
        demanda.visualizada = 0
        demanda.status = 'E'
        demanda.save()
        _thread.start_new_thread(send_mail, (request,))
        return redirect('prospeccao')
    except Exception:
        return redirect('prospeccao')

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