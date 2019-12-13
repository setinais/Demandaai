from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
import _thread
from demandai_administrador.models import Demand, Service, Laboratory, Equipment, Profile, Content, UserPermission, \
    Permission, UserContent, UserService, Institution, DemandCallback, Demandcb, Notification
from .forms import *
from datetime import datetime, timedelta
import os
from django.conf import settings

def logout_in(request):
    logout(request)
    return redirect('home')

@login_required
def home(request):
     try:

        notificacao = Notification.objects.filter(ulr='/adm/permission/'+str(request.user.id))
        solicitacao = False
        for notf in notificacao:
            solicitacao = notf
        dados = {
            'Total_servicos': Service.objects.count(),
            'Total_laboratorios': Laboratory.objects.count(),
            'Total_equipamentos': Equipment.objects.count(),
            'Total_profissionais': Profile.objects.filter(role='SE').count(),
            'Total_notificacao': Notification.objects.filter(profile_id=request.user.id,visualizada=0).count(),
            'servicos': Service.objects.all(),
            'userservice': UserService.objects.all(),
        }
        return render(request, 'administrador/home.html', {'dados': dados})
     except Exception:
        return render(request, 'site/error.html')

@login_required
def prospeccao(request):

    if request.user.has_permission('prospectar'):
        return redirect('home-adm')

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

        demandas = Demand.objects.filter(visualizada=1).order_by('-created_at')
        dados2 = []
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
            dados2.append(demanda)
            i += 1
        return render(request, 'administrador/prospeccao.html', {'dados': dados, 'dados2': dados2})
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
        'V': 'light',
        'B': 'dark',
    }[val]

@login_required
def encaminhar_demanda(request, action, id):

    if request.user.has_permission('prospectar'):
        return redirect('home-adm')

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
            prepare = {}
            dcb = Demandcb.objects.filter(action=action, action_id=actions[i].id, demand_id=id)
            if dcb.count() == 0:
                prepare = {
                    'id': actions[i].id,
                    'action': action,
                    'nome': actions[i].nome,
                    'status': actions[i].status,
                    'responsavel': actions[i].profile.username,
                    'unidade': actions[i].institution.nome,
                    'enviado': False
                }
                dados.append(prepare)
            elif dcb.first().aceita_rejeita is None:
                prepare = {
                    'id': actions[i].id,
                    'action': action,
                    'nome': actions[i].nome,
                    'status': actions[i].status,
                    'responsavel': actions[i].profile.username,
                    'unidade': actions[i].institution.nome,
                    'enviado': True
                }
                dados.append(prepare)
            i += 1
        return render(request, template, {'dados': dados, 'id_demanda': id})
    except Exception:
        return render(request, 'site/error.html')

@login_required
@require_http_methods(["GET"])
def encaminhar_demanda_acao(request):

    if request.user.has_permission('prospectar'):
        return redirect('home-adm')

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

        demanda.demandcallback_set.create(status='E', profile_id=request.user.id, feedback='Demanda encaminhada para "'+ action.nome+'", ficando em "análise"!', prazo_feedback=(datetime.today() + timedelta(days=2)))
        if request.GET['action'] == 'SER':
            for profile in action.userservice_set.all():
                Demandcb.objects.create(demand=demanda, action=request.GET['action'], action_id=action.id)
                Notification.objects.create(
                    titulo='Demanda',
                    texto='Foi enviada uma demanda para voçe!',
                    icone='fa fa-newspaper',
                    descricao=None,
                    ulr='/adm/demand',
                    visualizada=False,
                    profile_id=profile.profile_id,
                )
        else:
            Demandcb.objects.create(demand=demanda, action=request.GET['action'], action_id=action.id)
            Notification.objects.create(
                titulo='Demanda',
                texto='Foi enviada uma demanda para voçe!',
                icone='fa fa-newspaper',
                descricao=None,
                ulr='/adm/demand',
                visualizada=False,
                profile_id=action.profile.id,
            )
        _thread.start_new_thread(send_mail, (request,))
        return redirect('prospeccao')
    except Exception:
        return render(request, 'site/error.html')

@login_required
@require_http_methods(["GET"])
def encaminhar_demanda_acao_cancel(request):
    # if request.user.has_permission('prospectar'):
    #     return redirect('home-adm')
    #
    # try:
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
        demanda.status = 'S'
        demanda.save()

        dcb = Demandcb.objects.filter(demand=demanda, action=request.GET['action'], action_id=action.id).first()
        dcb.delete()
        demanda.demandcallback_set.create(status='E', profile_id=request.user.id, feedback='Demanda cancelada para "'+ action.nome+'"!', prazo_feedback=(datetime.today() + timedelta(days=2)))


        return redirect('prospeccao')
    # except Exception:
    #     return render(request, 'site/error.html')

@login_required
@require_http_methods(["GET"])
def rejeitar_demanda(request):

    if request.user.has_permission('prospectar'):
        return redirect('home-adm')

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

    if request.user.has_permission('prospectar'):
        if request.user.has_content('demand'):
            return redirect('home-adm')

    demanda = Demand.objects.get(id=id)
    demand_callback = []
    action = {}
    if demanda.action == 'SER':
        action = Service.objects.get(id=demanda.action_id)
    elif demanda.action == 'LAB':
        action = Laboratory.objects.get(id=demanda.action_id)
    elif demanda.action == 'EQU':
        action = Equipment.objects.get(id=demanda.action_id)
    for feedbc in demanda.demandcallback_set.order_by('-created_at'):
        demand_callback_dados = {
            'feedback': feedbc.feedback,
            'created_at': feedbc.created_at,
            'status': feedbc.get_status_display(),
            'badge': badge_select(feedbc.status),
            'id': feedbc.id
        }
        demand_callback.append(demand_callback_dados)
    dados = {
        'demanda': {
            'id': demanda.id,
            'action': demanda.action,
            'action_name': demanda.get_action_display(),
            'action_select': demanda.action_id,
            'setor': {
                'nome': action.nome,
                'responsavel': action.profile.__str__
            },
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
            response = HttpResponse(fh.read(), content_type="application/x-zip-compressed")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

@login_required
@require_http_methods(['POST'])
def responder_solicitante(request):
    _thread.start_new_thread(send_mail_responder_solicitante, (request,))
    demanda = Demand.objects.get(id=request.POST['id'])
    demanda.status = 'B'
    demanda.save()
    demanda.demandcallback_set.create(status='B', profile_id=request.user.id, feedback=request.POST['texto']+' ---- Aguardo do "FeedBack" do demandante!', prazo_feedback=(datetime.today() + timedelta(days=2)))

    return redirect('prospeccao')

#CRUD SERVIÇOES
@login_required
@require_http_methods(['GET'])
def servicos(request):

    if request.user.has_content('service'):
        return redirect('home-adm')

    servicos = Service.objects.all()
    return render(request,'administrador/servicos/home.html',{'servicos':servicos})

@login_required
def servicos_cadastro(request):

    if request.user.has_permission('add_service'):
        return redirect('home-adm')

    form = ServiceForm(request.POST or None)
    if form.is_valid():
        servico = form.save(commit=False)
        servico.status = 0
        servico.profile_id = request.user.id
        servico.save()
        return redirect('service')

    return render(request,'administrador/servicos/cadastro.html',{'form': form})

@login_required
def servicos_editar(request, id):

    if request.user.has_permission('update_service'):
        return redirect('home-adm')

    servico = Service.objects.get(id=id)
    form = ServiceForm(request.POST or None, instance=servico)

    if form.is_valid():
        form.save()
        return redirect('service')

    return render(request, 'administrador/servicos/cadastro.html', {'form': form,'dados': servico})

@login_required
def servicos_deletar(request, id):

    if request.user.has_permission('delete_service'):
        return redirect('home-adm')

    servico = Service.objects.get(id=id)
    servico.delete()
    return redirect('service')

@login_required
def servicos_receber(request, id):
    servico = Service.objects.get(id=id)
    for us in UserService.objects.all():
        if us.profile_id == request.user.id and servico.id == us.service_id:
            return redirect('home-adm')
    us = UserService.objects.create(profile_id=request.user.id,service_id=servico.id)
    us.save()
    return redirect('home-adm')

def servicos_cancelar(request, id):
    servico = Service.objects.get(id=id)
    for us in UserService.objects.all():
        if us.profile_id == request.user.id and servico.id == us.service_id:
            us.delete()
            return redirect('home-adm')

#CRUD EQUIPAMENTOS
@login_required
@require_http_methods(['GET'])
def equipamentos(request):

    if request.user.has_content('equipament'):
        return redirect('home-adm')

    equipamentos = Equipment.objects.all()
    return render(request,'administrador/equipamentos/home.html',{'equipamentos':equipamentos})

@login_required
def equipamentos_cadastro(request):

    if request.user.has_permission('add_equipament'):
        return redirect('home-adm')

    form = EquipamentForm(request.POST or None)
    if form.is_valid():
        equipamento = form.save(commit=False)
        equipamento.status = 0
        equipamento.profile_id = request.user.id
        equipamento.save()
        return redirect('equipament')

    return render(request,'administrador/equipamentos/cadastro.html',{'form': form})

@login_required
def equipamentos_editar(request, id):

    if request.user.has_permission('update_equipament'):
        return redirect('home-adm')

    Equipmente = Equipment.objects.get(id=id)
    form = EquipamentForm(request.POST or None, instance=Equipmente)
    if form.is_valid():
        form.save()
        return redirect('equipament')
    return render(request, 'administrador/equipamentos/cadastro.html', {'form': form,'dados': Equipmente})

@login_required
def equipamentos_deletar(request, id):

    if request.user.has_permission('delete_equipament'):
        return redirect('home-adm')

    equipamento = Equipment.objects.get(id=id)
    equipamento.delete()
    return redirect('equipament')

#CRUD LABORATORIO
@login_required
@require_http_methods(['GET'])
def laboratorios(request):

    if request.user.has_content('laboratory'):
        return redirect('home-adm')

    laboratorios = Laboratory.objects.all()
    return render(request,'administrador/laboratorios/home.html',{'laboratorios': laboratorios})

@login_required
def laboratorios_cadastro(request):

    if request.user.has_permission('add_laboratory'):
        return redirect('home-adm')

    form = LaboratoryForm(request.POST or None)
    if form.is_valid():
        laboratorio = form.save(commit=False)
        laboratorio.pesquisa_extensao = False
        #laboratorio.profile_id = request.user.id
        laboratorio.status = 0
        laboratorio.save()
        return redirect('laboratory')

    return render(request,'administrador/laboratorios/cadastro.html',{'form': form})

@login_required
def laboratorios_editar(request, id):

    if request.user.has_permission('update_laboratory'):
        return redirect('home-adm')

    lab = Laboratory.objects.get(id=id)
    form = LaboratoryForm(request.POST or None, instance=lab)
    if form.is_valid():
        form.save()
        return redirect('laboratory')
    return render(request, 'administrador/laboratorios/cadastro.html', {'form': form,'dados': lab})

@login_required
def laboratorios_deletar(request, id):

    if request.user.has_permission('delete_laboratory'):
        return redirect('home-adm')

    laboratorio = Laboratory.objects.get(id=id)
    laboratorio.delete()
    return redirect('laboratory')

# CRUD PROFILE
@login_required
@require_http_methods(['GET'])
def profile(request):

    if request.user.has_content('profile'):
        return redirect('home-adm')

    profile = Profile.objects.all().filter(deleted=None)
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
def profile_editar(request):
    pro = Profile.objects.get(id=request.user.id)
    pro.password = ''
    form = ProfileForm(request.POST or None, instance=pro)
    if form.is_valid():
        pro = form.save()
        pro.set_password(pro.password)
        pro.save()
        update_session_auth_hash(request, pro)
        return redirect('home-adm')
    return render(request, 'administrador/profile/cadastro.html', {'form': form,'dados': pro})

def profile_desativar(request):
    pro = Profile.objects.get(id=request.user.id)
    pro.is_active = 0
    pro.delete()
    pro.save()
    return redirect('home')

@login_required
def profile_deletar(request, id):

    if request.user.has_permission('delete_usuario'):
        return redirect('home-adm')

    profile = Profile.objects.get(id=id)
    profile.delete()

    return redirect('profile')

# Permissões
@login_required
def permission(request, id):

    if request.user.has_permission('view_permission'):
        return redirect('home-adm')

    profile = Profile.objects.get(id=id)
    permissoes = Content.objects.order_by('id')
    notificacao = Notification.objects.filter(ulr='/adm/permission/'+str(id))
    notficacao = False
    for notf in notificacao:
        notficacao = notf
    return render(request, 'administrador/permission/permission.html', {'profile': profile, 'permissoes': permissoes,'notificacao':notficacao})

def permission_edit(request, id):

    if request.user.has_permission('update_permission'):
        return redirect('home-adm')

    # Adicionar as permissões selecionadas
    dados = request.POST
    menu = []
    check_qntd_permissions = []
    for d in dados:
        if 'csrfmiddlewaretoken' != d:
            if 1 <= int(d):
                if int(d) <= 26:
                    u = UserPermission.objects.filter(user_id=id, permission_id=d)
                    if u.count() == 0:
                        u = UserPermission(user_id=id, permission_id=d)
                        u.save()
                        menu.append(u.permission.content.id)
                        check_qntd_permissions.append(u.permission_id)
                    else:
                        menu.append(u[0].permission.content.id)
                        check_qntd_permissions.append(u[0].permission_id)
    l = []
    for i in menu:
        if i not in l:
            l.append(i)
    l.sort()

    for m in l:
        c = UserContent.objects.filter(profile_id=id, content_id=m)
        if c.count() == 0:
            c = UserContent(profile_id=id, content_id=m)
            c.save()

    all_permission_now = UserPermission.objects.filter(user_id=id)
    # Apagar permissões retiradas
    for permissao_tirar in all_permission_now:
        check = True
        for permissao_atual in check_qntd_permissions:
            if permissao_tirar.permission.id == int(permissao_atual):
                check = False
                break
        if check:
            permissao_tirar.delete()

    all_content_now = UserContent.objects.filter(profile_id=id)
    for content_tirar in all_content_now:
        check = True
        for content_atual in l:
            if content_tirar.content.id == int(content_atual):
                check = False
        if check:
            content_tirar.delete()

    return redirect('profile')

@login_required
@require_http_methods(['POST'])
def permission_solicitacao(request):
    permis = Permission.objects.get(codigo='update_permission')
    usp = UserPermission.objects.filter(permission_id=permis.id)
    for users in usp:
        Notification.objects.create(
                    titulo='Uma solcitada',
                    texto='O usuario:<b>'+request.user.first_name+' '+request.user.last_name+'</b> solicitou permissões!',
                    icone='fa fa-lock',
                    descricao=request.POST['descricao'],
                    ulr='/adm/permission/'+str(request.user.id),
                    visualizada=False,
                    profile_id=users.user_id,
                )
    return redirect('home-adm')

# CRUD INSTITUIÇÂO
@login_required
@require_http_methods(['GET'])
def institution(request):

    if request.user.has_content('institution'):
        return redirect('home-adm')

    institution = Institution.objects.all()
    return render(request,'administrador/institution/home.html',{'institutions': institution})

def institution_cadastro(request):

    if request.user.has_permission('add_institution'):
        return redirect('home-adm')

    form = InstitutionForm(request.POST or None)
    if form.is_valid():
        institution = form.save(commit=False)
        institution.set_password(profile.password)
        institution.is_superuser = 0
        institution.save()
        return redirect('institution')

    return render(request,'administrador/institution/cadastro.html',{'form': form})

@login_required
def institution_editar(request, id):

    if request.user.has_permission('update_institution'):
        return redirect('home-adm')

    pro = Institution.objects.get(id=id)
    form = InstitutionForm(request.POST or None, instance=pro)
    if form.is_valid():
        form.save()
        return redirect('institution')
    return render(request, 'administrador/institution/cadastro.html', {'form': form,'dados': pro})

@login_required
def institution_deletar(request, id):

    if request.user.has_permission('delete_institution'):
        return redirect('home-adm')

    institution = Institution.objects.get(id=id)
    institution.delete()
    return redirect('institution')

# Demands
@login_required
def demand(request):

    if request.user.has_content('demand'):
        return redirect('home-adm')

    try:
        services = UserService.objects.filter(profile_id=request.user.id)
        laboratorys = Laboratory.objects.filter(profile_id=request.user.id)
        equipments = Equipment.objects.filter(profile_id=request.user.id)

        md = []
        s = []
        l = []
        e = []

        # Get Demandas vinculadas aos serviços
        for service in services:
            demandcbs = Demandcb.objects.filter(action='SER', action_id=service.service_id, aceita_rejeita=None)
            demandcbs2 = Demandcb.objects.filter(action='SER', action_id=service.service_id, aceita_rejeita=1)
            for demandcb in demandcbs:
                dados = {
                    'id': demandcb.demand.id,
                    'id_cb': demandcb.id,
                    'setor': service.service.nome,
                    'ar': demandcb.aceita_rejeita,
                    'nome': demandcb.demand.nome,
                    'descricao': demandcb.demand.descricao,
                    'created_at': demandcb.demand.created_at,
                }
                s.append(dados)
            for demandcb in demandcbs2:
                dados = {
                    'id': demandcb.demand.id,
                    'id_cb': demandcb.id,
                    'ar': demandcb.aceita_rejeita,
                    #'setor': service.nome,
                    'type_sector': 'Serviço',
                    'status': demandcb.demand.get_status_display(),
                    'badge': badge_select(demandcb.demand.status),
                    'nome': demandcb.demand.nome,
                    'descricao': demandcb.demand.descricao,
                    'created_at': demandcb.demand.created_at,
                }
                md.append(dados)
        # Get Demandas vinculadas aos Laboratorios
        for laboratory in laboratorys:
            demandcbs = Demandcb.objects.filter(action='LAB', action_id=laboratory.id, aceita_rejeita=None)
            demandcbs2 = Demandcb.objects.filter(action='LAB', action_id=laboratory.id, aceita_rejeita=1)
            for demandcb in demandcbs:
                dados = {
                    'id': demandcb.demand.id,
                    'id_cb': demandcb.id,
                    'setor': laboratory.nome,
                    'ar': demandcb.aceita_rejeita,
                    'nome': demandcb.demand.nome,
                    'descricao': demandcb.demand.descricao,
                    'created_at': demandcb.demand.created_at,
                }
                l.append(dados)
            for demandcb in demandcbs2:
                dados = {
                    'id': demandcb.demand.id,
                    'id_cb': demandcb.id,
                    'ar': demandcb.aceita_rejeita,
                    'setor': laboratory.nome,
                    'status': demandcb.demand.get_status_display(),
                    'badge': badge_select(demandcb.demand.status),
                    'type_sector': 'Laboratorio',
                    'nome': demandcb.demand.nome,
                    'descricao': demandcb.demand.descricao,
                    'created_at': demandcb.demand.created_at,
                }
                md.append(dados)


        # Get Demandas vinculadas aos Equipamentos
        for equipment in equipments:
            demandcbs = Demandcb.objects.filter(action='EQU', action_id=equipment.id, aceita_rejeita=None)
            demandcbs2 = Demandcb.objects.filter(action='EQU', action_id=equipment.id, aceita_rejeita=1)
            for demandcb in demandcbs:
                dados = {
                    'id': demandcb.demand.id,
                    'id_cb': demandcb.id,
                    'ar': demandcb.aceita_rejeita,
                    'setor': equipment.nome,
                    'nome': demandcb.demand.nome,
                    'descricao': demandcb.demand.descricao,
                    'created_at': demandcb.demand.created_at,
                }
                e.append(dados)
            for demandcb in demandcbs2:
                dados = {
                    'id': demandcb.demand.id,
                    'id_cb': demandcb.id,
                    'ar': demandcb.aceita_rejeita,
                    'type_sector': 'Equipamento',
                    'status': demandcb.demand.get_status_display(),
                    'badge': badge_select(demandcb.demand.status),
                    'setor': equipment.nome,
                    'nome': demandcb.demand.nome,
                    'descricao': demandcb.demand.descricao,
                    'created_at': demandcb.demand.created_at,
                }
                md.append(dados)

        ct = {'s': len(s), 'l': len(l), 'e': len(e), 'md': len(md)}
        return render(request, 'administrador/demands/home.html', {'my_demands': md,'services': s, 'laboratorys': l, 'equipments': e, 'counts': ct})
    except Exception:
        return render(request, 'site/error.html')

@login_required
def demand_ar(request, ar, id):

    if request.user.has_permission('update_demand'):
        return redirect('home-adm')

    try:
        demandcb = Demandcb.objects.get(id=id)
        demandcb.aceita_rejeita = ar
        action = {}
        if demandcb.action == 'SER':
            action = Service.objects.get(id=demandcb.action_id)
        elif demandcb.action == 'LAB':
            action = Laboratory.objects.get(id=demandcb.action_id)
        elif demandcb.action == 'EQU':
            action = Equipment.objects.get(id=demandcb.action_id)
        if int(ar) == 1:
            demandcb.demand.status = 'A'
            demandcb.demand.demandcallback_set.create(status='A', profile_id=request.user.id,
                                              feedback='Demanda aceita por "' + action.nome + '"!',
                                              prazo_feedback=(datetime.today() + timedelta(days=2)))

        else:
            demandcb.demand.status = 'R'
            demandcb.demand.demandcallback_set.create(status='R', profile_id=request.user.id,
                                              feedback='Demanda recusada por "' + action.nome + '"!',
                                              prazo_feedback=(datetime.today() + timedelta(days=2)))
        demandcb.demand.action = demandcb.action
        demandcb.demand.action_id = demandcb.action_id
        demandcb.demand.visualizada = 1
        demandcb.demand.save()
        demandcb.save()

        return redirect('demand')
    except Exception:
        return render(request, 'site/error.html')

@login_required
def atualizacao_demand(request):
    if request.user.has_permission('update_demand'):
        return redirect('home-adm')

    try:
        demanda = Demand.objects.get(id=request.POST['id'])

        action = {}
        if demanda.action == 'SER':
            action = Service.objects.get(id=demanda.action_id)
        elif demanda.action == 'LAB':
            action = Laboratory.objects.get(id=demanda.action_id)
        elif demanda.action == 'EQU':
            action = Equipment.objects.get(id=demanda.action_id)

        texto = ''
        if request.POST['status'] == 'A':
            texto = 'Duvida encaminhada para o demandante!'
        elif request.POST['status'] == 'P':
            texto = 'Demanda começou a ser produzida!'
        elif request.POST['status'] == 'R':
            texto = 'Demanda cancelada por "'+action.nome+'"!'
        elif request.POST['status'] == 'F':
            texto = 'Demanda concluida por "'+action.nome+'"!'
        demanda.status = request.POST['status']
        demanda.demandcallback_set.create(status=request.POST['status'], profile_id=request.user.id,
                                                      feedback=texto,
                                                      prazo_feedback=(datetime.today() + timedelta(days=2)))

        demanda.save()

        return redirect('demand')
    except Exception:
        return render(request, 'site/error.html')

@login_required
def notificacao(request, id):
    notfi = Notification.objects.get(id=id)
    if notfi.profile_id == request.user.id:
        notfi.visualizada = 1
        notfi.save()
    return redirect(notfi.ulr)