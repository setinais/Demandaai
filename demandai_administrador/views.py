from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect

from demandai_administrador.models import Demand, Service, Laboratory, Equipment

@login_required
def home(request):
    return render(request, 'administrador/home.html', {'user': request.user.is_authenticated})

@login_required
def prospeccao(request):

    demandas = Demand.objects.filter(status='S').order_by('-created_at')
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
    template = ''
    actions = []
    if action == 'SER':
        template = 'administrador/encaminhar_demanda/servico.html'
        actions = Service.objects.filter(status=0)
    elif action == 'LAB':
        template = 'administrador/encaminhar_demanda/laboratorio.html'
    elif action == 'EQU':
        template = 'administrador/encaminhar_demanda/equipamento.html'
    else:
        return HttpResponseNotFound('<h1>Erro Interno 500</h1>')

    i=0
    dados = []
    while i < len(actions):
        prepare = {
            'id': actions[i].id,
            'nome': actions[i].nome,
            'responsavel': actions[i].profile.username,
            'id_demanda': id
        }
        dados.append(prepare)
        i += 1

    return render(request, template, {'dados': dados})