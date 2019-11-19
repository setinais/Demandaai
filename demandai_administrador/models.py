from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE

# Create your models here.
from demandai_site.validators import validate_file_size


class Institution(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    nome = models.CharField(max_length=60)
    email = models.EmailField(max_length=50, unique=True)
    descricao = models.TextField()
    phone = models.CharField(max_length=30)
    site = models.CharField(max_length=60)
    status = models.BooleanField()
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=11)
    sector = models.CharField(max_length=60)
    city = models.CharField(max_length=30)
    complement = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nome



class Profile(AbstractUser, SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    roles = (
        ('AD', 'Administrador'),
        ('SE', 'Servidor'),
        ('PE', 'Proex'),
        ('DI', 'Diem'),
        ('PI', 'Propi'),
        ('TE', 'Técnico'),
    )
    username = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=60, unique=True)
    role = models.CharField(max_length=2, choices=roles, default='SE')
    institution = models.ForeignKey(Institution, related_name='profile', on_delete=models.PROTECT, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Laboratory(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    profile = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='laboratories', on_delete=models.PROTECT)
    telefone = models.CharField(max_length=14)
    descricao = models.TextField()
    nome = models.CharField(max_length=30)
    atividades_realizadas = models.TextField()
    pesquisa_extensao = models.BooleanField()
    institution = models.ForeignKey(Institution, related_name='laboratories', on_delete=models.PROTECT)
    endereco_sala = models.CharField(max_length=40)
    servidores = models.TextField()
    departamentos = models.TextField()
    cursos = models.TextField()
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nome


class Equipment(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    profile = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='equipments', on_delete=models.PROTECT)
    codigo = models.CharField(max_length=9)
    descricao = models.TextField()
    nome = models.CharField(max_length=30)
    institution = models.ForeignKey(Institution, related_name='equipments', on_delete=models.PROTECT)
    laboratory = models.ForeignKey(Laboratory, related_name='equipments', on_delete=models.SET_NULL, null=True)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nome



class Service(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    profile = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='services', on_delete=models.PROTECT)
    plataformas = models.TextField()
    descricao = models.TextField()
    nome = models.CharField(max_length=30)
    servidores = models.TextField()
    desenvolvedores = models.TextField()
    departamentos = models.TextField()
    institution = models.ForeignKey(Institution, related_name='services', on_delete=models.SET_NULL, null=True)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nome



class Demand(SafeDeleteModel):
    actions = (
        ('SER', 'Serviço'),
        ('LAB', 'Laboratorio'),
        ('EQU', 'Equipamento'),
    )
    status = (
        ('S', 'Solicitado'),
        ('E', 'Analise'),
        ('R', 'Recusada'),
        ('A', 'Aceita'),
        ('P', 'Produção'),
        ('F', 'Finalizada'),
    )
    action = models.CharField(max_length=3, choices=actions)
    action_id = models.IntegerField()
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=16, null=True, blank=True)
    codigo = models.CharField(max_length=6)
    email = models.EmailField(max_length=40)
    descricao = models.TextField()
    # cpf = models.CharField(max_length=20)
    # data_nascimento = models.DateField()
    status = models.CharField(max_length=1, choices=status, default='S')
    file = models.FileField(upload_to="images/demand_files", null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['zip', 'rar']), validate_file_size])
    visualizada = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    _safedelete_policy = SOFT_DELETE_CASCADE

class DemandCallback(SafeDeleteModel):
    actions = (
        ('SER', 'Serviço'),
        ('LAB', 'Laboratorio'),
        ('EQU', 'Equipamento'),
    )

    demand = models.ForeignKey(Demand, related_name='demand_callback', on_delete=models.PROTECT)
    action = models.CharField(max_length=3, choices=actions)
    action_id = models.IntegerField()
    feedback = models.TextField()
    prazo_feedback = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)