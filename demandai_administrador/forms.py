from django import forms
from django.contrib.sites.shortcuts import get_current_site

from demandai_administrador.models import Service, Laboratory, Equipment, Demand, Profile, Institution, Notification
from .mail import send_mail_template

def send_mail(request):
    subject = 'Demanda'
    message = 'Serviço'
    action = {}
    if request.GET['action'] == 'SER':
        action = Service.objects.get(id=request.GET['id'])
    elif request.GET['action'] == 'LAB':
        action = Laboratory.objects.get(id=request.GET['id'])
    elif request.GET['action'] == 'EQU':
        action = Equipment.objects.get(id=request.GET['id'])
    demanda = Demand.objects.get(id=request.GET['id_demanda'])
    context = {
        'nome': action.profile.username,
        'descricao': demanda.descricao,
        'action': demanda.nome,
        'domain': get_current_site(request),
        'id_demanda': demanda.id
    }
    message = message % context

    send_mail_template(subject, 'administrador/email_prospeccao.html', context, [action.profile.email])

def send_mail_responder_solicitante(request):
    subject = 'Demanda'
    message = 'Serviço'
    demanda = Demand.objects.get(id=request.POST['id'])
    context = {
        'nome': demanda.nome,
        'domain': get_current_site(request),
        'texto': request.POST['texto']
    }
    message = message % context

    send_mail_template(subject, 'administrador/email_responder_solicitante.html', context, [demanda.email])

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['nome','plataformas','descricao','desenvolvedores','departamentos','institution']

class EquipamentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['codigo','nome','descricao','institution','laboratory']

class LaboratoryForm(forms.ModelForm):
    class Meta:
        model = Laboratory
        fields = ['nome','servidores', 'telefone','descricao','atividades_realizadas','endereco_sala','departamentos', 'cursos', 'institution','profile']

class ProfileForm(forms.ModelForm):

    password = forms.CharField(label='Nova Senha',widget=forms.PasswordInput())

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'institution', 'password']

class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ['nome', 'email', 'phone', 'descricao', 'city', 'site', 'street', 'number', 'sector', 'complement']