from django import forms
from django.core.mail import send_mail
from django.conf import settings
from demandai_administrador.models import Demand

from .mail import send_mail_template

class DemandForm(forms.ModelForm):
    class Meta:
        model = Demand
        fields = ['nome', 'cpf', 'data_nascimento', 'email', 'telefone', 'descricao', 'action', 'action_id']

    def send_mail(self, request):
        subject = '[%s] Contato' % request
        message = 'Nome: %(name)s; E-mail: %(email)s; %(message)s'
        context = {
            'name': 'ddddddd',
            'email': 'dddddd',
            'message': 'okoggggggggggggggggggggggggggk',
        }
        message = message % context

        send_mail_template(subject, 'site/email_demanda.html', context, [settings.CONTACT_EMAIL])