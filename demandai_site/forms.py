from django import forms
from django.core.mail import send_mail
from django.conf import settings
from django.forms import widgets

from demandai_administrador.models import Demand, User

from .mail import send_mail_template

class DemandForm(forms.ModelForm):
    class Meta:
        model = Demand
        fields = ['nome', 'cpf', 'data_nascimento', 'email', 'telefone', 'descricao', 'action', 'action_id', 'codigo']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vinnicyus Carvalho Gonçalves'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '999.999.999-99'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': '01/02/2000', 'type': 'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@example.com'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '99 9 9999-9999'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control input-message', 'placeholder': 'Descricao da demanda'}),
            'action': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}),
            'action_id': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'})
        }


    def send_mail(self, request, email):
        subject = '[%s] Contato' % request
        message = 'Nome: %(name)s; E-mail: %(email)s; %(message)s'
        context = {
            'name': 'ddddddd',
            'email': 'dddddd',
            'message': 'okoggggggggggggggggggggggggggk',
        }
        message = message % context

        send_mail_template(subject, 'site/email_demanda.html', context, email)

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'email': forms.TextInput(attrs={'class': 'web form-control', 'placeholder': 'example@example.com'}),
            'password': forms.PasswordInput(attrs={'class': 'Password form-control', 'placeholder': 'senha', 'type': 'password'}),
        }