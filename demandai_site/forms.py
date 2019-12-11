from django import forms
from django.contrib.sites.shortcuts import get_current_site

from demandai_administrador.models import Demand, Profile, Service, Laboratory, Equipment, Institution

from .mail import send_mail_template

class DemandForm(forms.ModelForm):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control'}), required=False)
    telefone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'opcional'}), required=False)

    class Meta:
        model = Demand
        fields = ['nome', 'email', 'descricao', 'action', 'action_id', 'codigo', 'file', 'telefone']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Informe o seu nome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'exemplo@exemplo.com'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control input-message', 'placeholder': 'Descrição da demanda'}),
            'action': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}),
            'action_id': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'})
        }


    def send_mail(self, request):
        current_site = get_current_site(request)
        subject = 'Contato'
        message = 'Serviço'
        action = {}
        if self.cleaned_data['action'] == 'SER':
            action = Service.objects.get(id=self.cleaned_data['action_id'])
        elif self.cleaned_data['action'] == 'LAB':
            action = Laboratory.objects.get(id=self.cleaned_data['action_id'])
        elif self.cleaned_data['action'] == 'EQU':
            action = Equipment.objects.get(id=self.cleaned_data['action_id'])
        context = {
            'nome': self.cleaned_data['nome'],
            'descricao': self.cleaned_data['descricao'],
            'action': action.nome,
            'email': self.cleaned_data['email'],
            'codigo': self.cleaned_data['codigo'],
            'domain': current_site.domain
        }
        message = message % context

        send_mail_template(subject, 'site/email_demanda.html', context, [self.cleaned_data['email']])

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),label='Senha')
    confirm_password = forms.CharField(widget=forms.PasswordInput(),label='Comfirme a senha')
    institution = forms.ModelChoiceField(queryset=Institution.objects.all(),widget=forms.Select(attrs={'style':'padding: 10px'}),required=True)
    first_name = forms.CharField(required=True,label='Primeiro nome')
    last_name = forms.CharField(required=True,label='Sobrenome')
    username = forms.CharField(required=True,label='Nome de Úsuario')
    class Meta:
        model = Profile
        fields = ['institution','first_name','last_name','username', 'email','password']

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError(
                "As senhas não coincidem!"
            )