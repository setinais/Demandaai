from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
import _thread
from demandai_administrador.models import Demand, Service, Laboratory, Equipment, Profile, Content, UserPermission, Permission
from .forms import *
from datetime import datetime, timedelta
import os
from django.conf import settings

def logout_in(request):
    logout(request)
    return redirect('home')

@login_required
def home(request):
    # try:
        dados = {
            'servicos': Service.objects.count(),
            'laboratorios': Laboratory.objects.count(),
            'equipamentos': Equipment.objects.count(),
            'profissionais': Profile.objects.filter(role='SE').count(),
        }
        return render(request, 'administrador/home.html', {'dados': dados})
    # except Exception:
    #     return render(request, 'site/error.html')


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
                'action_sel': demandas[i].action,
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
    # try:
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
    # except Exception:
    #     return render(request, 'site/error.html')

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
            'action_select': demanda.action_id,
            'nome': demanda.nome,
            'email': demanda.email,
            'file': demanda.file,
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
        'time_now': datetime.now(),
    }
    return render(request, 'administrador/demanda_detalhes.html', {'dados': dados})

@login_required
@require_http_methods(['GET'])
def download_arquivos(request):
    demanda = Demand.objects.get(id=request.GET['path'])
    file_path = os.path.join(settings.MEDIA_ROOT, demanda.file.name)
    if os.path.exists(file_path):
        with open(file_path, 'wb') as fh:
            response = HttpResponse(fh.read(), content_type="application/x-rar-compressed")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

@login_required
@require_http_methods(['POST'])
def responder_solicitante(request):
    _thread.start_new_thread(send_mail_responder_solicitante, (request,))
    demanda = Demand.objects.get(id=request.POST['id'])
    demanda.status = 'R'
    demanda.demand_callback.create(action=demanda.action, action_id=demanda.action_id, feedback=request.POST['texto'],
                                   prazo_feedback=(datetime.today() + timedelta(days=2)))
    demanda.save()
    return redirect('prospeccao')

#CRUD SERVIÇOES
@login_required
@require_http_methods(['GET'])
def servicos(request):
    servicos = Service.objects.all()
    return render(request,'administrador/servicos/home.html',{'servicos':servicos})

@login_required
def servicos_cadastro(request):
    form = ServiceForm(request.POST or None)
    if form.is_valid():
        servico = form.save(commit=False)
        servico.profile_id = request.user.id
        servico.status = 1
        servico.save()
        return redirect('service')

    return render(request,'administrador/servicos/cadastro.html',{'form': form})

@login_required
def servicos_editar(request, id):
    servico = Service.objects.get(id=id)
    form = ServiceForm(request.POST or None, instance=servico)

    if form.is_valid():
        form.save()
        return redirect('service')

    return render(request, 'administrador/servicos/cadastro.html', {'form': form,'dados': servico})

@login_required
def servicos_deletar(request, id):
    servico = Service.objects.get(id=id)
    servico.delete()
    return redirect('service')
#END CRUD SERVIÇOS

#CRUD EQUIPAMENTOS
@login_required
@require_http_methods(['GET'])
def equipamentos(request):
    equipamentos = Equipment.objects.all()
    return render(request,'administrador/equipamentos/home.html',{'equipamentos':equipamentos})

@login_required
def equipamentos_cadastro(request):
    form = EquipamentForm(request.POST or None)
    if form.is_valid():
        equipamento = form.save(commit=False)
        equipamento.profile_id = request.user.id
        equipamento.status = 1
        equipamento.save()
        return redirect('equipament')

    return render(request,'administrador/equipamentos/cadastro.html',{'form': form})

@login_required
def equipamentos_editar(request, id):
    Equipmente = Equipment.objects.get(id=id)
    form = EquipamentForm(request.POST or None, instance=Equipmente)
    if form.is_valid():
        form.save()
        return redirect('equipament')
    return render(request, 'administrador/equipamentos/cadastro.html', {'form': form,'dados': Equipmente})

@login_required
def equipamentos_deletar(request, id):
    equipamento = Equipment.objects.get(id=id)
    equipamento.delete()
    return redirect('equipament')

#END CRUD EQUIPAMENTOS

#CRUD LABORATORIO
@login_required
@require_http_methods(['GET'])
def laboratorios(request):
    laboratorios = Laboratory.objects.all()
    return render(request,'administrador/laboratorios/home.html',{'laboratorios': laboratorios})

@login_required
def laboratorios_cadastro(request):
    form = LaboratoryForm(request.POST or None)
    if form.is_valid():
        laboratorio = form.save(commit=False)
        laboratorio.pesquisa_extensao = False
        laboratorio.profile_id = request.user.id
        laboratorio.status = 1
        laboratorio.save()
        return redirect('laboratory')

    return render(request,'administrador/laboratorios/cadastro.html',{'form': form})

@login_required
def laboratorios_editar(request, id):
    lab = Laboratory.objects.get(id=id)
    form = LaboratoryForm(request.POST or None, instance=lab)
    if form.is_valid():
        form.save()
        return redirect('laboratory')
    return render(request, 'administrador/laboratorios/cadastro.html', {'form': form,'dados': lab})

@login_required
def laboratorios_deletar(request, id):
    laboratorio = Laboratory.objects.get(id=id)
    laboratorio.delete()
    return redirect('laboratory')

# CRUD PROFILE
@login_required
@require_http_methods(['GET'])
def profile(request):
    profile = Profile.objects.all()
    return render(request,'administrador/profile/home.html',{'profiles': profile})

def profile_cadastro(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        profile = form.save(commit=False)
        profile.set_password(profile.password)
        profile.is_superuser = 0
        profile.save()
        return redirect('laboratory')

    return render(request,'administrador/profile/cadastro.html',{'form': form})

@login_required
def profile_editar(request, id):
    pro = Profile.objects.get(id=id)
    form = ProfileForm(request.POST or None, instance=pro)
    if form.is_valid():
        form.save()
        return redirect('laboratory')
    return render(request, 'administrador/profile/cadastro.html', {'form': form,'dados': pro})

@login_required
def profile_deletar(request, id):
    profile = Profile.objects.get(id=id)
    profile.delete()
    return redirect('laboratory')

# Permissões

@login_required
def permission(request, id):
    profile = Profile.objects.get(id=id)
    permissoes = Content.objects.order_by('id')
    return render(request, 'administrador/permission/permission.html', {'profile': profile, 'permissoes': permissoes})

def permission_edit(request, id):
    dados = request.POST
    menu = []
    for d in dados:
        if 'csrfmiddlewaretoken' != d:
            if 1 <= int(d):
                if int(d) <= 26:
                    u = UserPermission.objects.filter(user_id=id, permission_id=d)
                    if u.count() == 0:
                        u = UserPermission(user_id=id, permission_id=d)
                        # u.save()
                        menu.append(u.permission.content.id)
    menu.sort()
    return redirect('profile')