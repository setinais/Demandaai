from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import HARD_DELETE_NOCASCADE

# Create your models here.
class Institution(SafeDeleteModel):
    _safedelete_policy = HARD_DELETE_NOCASCADE

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



class User(SafeDeleteModel):
    _safedelete_policy = HARD_DELETE_NOCASCADE
    roles = (
        ('AD', 'Administrador'),
        ('SE', 'Servidor'),
        ('PE', 'Proex'),
        ('DI', 'Diem'),
        ('PI', 'Propi'),
        ('TE', 'Técnico'),
    )
    nome = models.CharField(max_length=30)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=2, choices=roles)
    institution = models.ForeignKey(Institution, related_name='users', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Action(SafeDeleteModel):
    _safedelete_policy = HARD_DELETE_NOCASCADE

    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=30)
    icon = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class AccessControl(SafeDeleteModel):
    _safedelete_policy = HARD_DELETE_NOCASCADE

    action = models.ForeignKey(Action, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create = models.BooleanField()
    update = models.BooleanField()
    delete = models.BooleanField()
    select = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Laboratory(SafeDeleteModel):
    _safedelete_policy = HARD_DELETE_NOCASCADE

    user = models.ForeignKey(User, related_name='laboratories', on_delete=models.PROTECT)
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



class Equipment(SafeDeleteModel):
    _safedelete_policy = HARD_DELETE_NOCASCADE

    user = models.ForeignKey(User, related_name='equipments', on_delete=models.PROTECT)
    codigo = models.CharField(max_length=9)
    descricao = models.TextField()
    nome = models.CharField(max_length=30)
    institution = models.ForeignKey(Institution, related_name='equipments', on_delete=models.PROTECT)
    laboratory = models.ForeignKey(Laboratory, related_name='equipments', on_delete=models.SET_NULL, null=True)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Service(SafeDeleteModel):
    _safedelete_policy = HARD_DELETE_NOCASCADE

    user = models.ForeignKey(User, related_name='services', on_delete=models.PROTECT)
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



class Demand(SafeDeleteModel):
    _safedelete_policy = HARD_DELETE_NOCASCADE

    actions = (
        ('SER', 'Serviços'),
        ('LAB', 'Laboratorios'),
        ('EQU', 'Equipamentos'),
    )
    action = models.CharField(max_length=3, choices=actions)
    action_id = models.IntegerField()
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)
    codigo = models.CharField(max_length=9)
    email = models.EmailField(max_length=40)
    descricao = models.TextField()
    cpf = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    visualizada = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



