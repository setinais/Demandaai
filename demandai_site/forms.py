from django import forms
from django.contrib.sites.shortcuts import get_current_site

from demandai_administrador.models import Demand, User, Action

from .mail import send_mail_template

class DemandForm(forms.ModelForm):
    class Meta:
        model = Demand
        fields = ['nome', 'cpf', 'data_nascimento', 'email', 'telefone', 'descricao', 'action', 'action_id', 'codigo']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Informe o seu nome'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '999.999.999-99'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa', 'type': 'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'exemplo@exemplo.com'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '99 9 9999-9999'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control input-message', 'placeholder': 'Descrição da demanda'}),
            'action': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}),
            'action_id': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'})
        }

    def send_mail(self, request):
        current_site = get_current_site(request)
        print(current_site.domain)
        subject = 'Contato'
        message = 'Serviço'
        context = {
            'nome': self.cleaned_data['nome'],
            'descricao': self.cleaned_data['descricao'],
            'action': Action.objects.get(pk=self.cleaned_data['action_id']).nome,
            'cpf': self.cleaned_data['cpf'],
            'codigo': self.cleaned_data['codigo'],
            'domain': current_site.domain
        }
        message = message % context

        send_mail_template(subject, 'site/email_demanda.html', context, [self.cleaned_data['email']])

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'email': forms.TextInput(attrs={'class': 'web form-control', 'placeholder': 'example@example.com'}),
            'password': forms.PasswordInput(attrs={'class': 'Password form-control', 'placeholder': 'senha', 'type': 'password'}),
        }
