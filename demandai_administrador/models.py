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
    institution = models.ForeignKey(Institution, on_delete=models.PROTECT, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def has_permission(self, codigo):
        permissao = Permission.objects.filter(codigo=codigo)
        permissions_user = UserPermission.objects.filter(user_id=self.id, permission_id=permissao.id)
        return permissions_user.count() > 0

    @property
    def my_permissions(self):
        grop = []
        p = []
        dados = []
        contents = UserContent.objects.filter(profile=self.id).order_by('content')
        permissoes = UserPermission.objects.filter(user=self.id).order_by('permission')
        for cont in contents:
            content = Content.objects.get(id=cont.content_id)
            grop.append(content.model)

        for per in permissoes:
            permissao = Permission.objects.get(id=per.permission_id)
            grop.append(permissao.codigo)
        dados.append(grop)
        dados.append(p)
        return dados
    @property
    def permissions_for_menu(self):
        permissoes = UserContent.objects.filter(profile=self.id).order_by('content')
        dados = []
        for permissao in permissoes:
            content = Content.objects.get(id=permissao.content_id)
            dados.append(content)
        return dados
    def permissions_for_menu_count(self):
        permissoes = UserContent.objects.filter(profile=self.id).order_by('content')
        dados = 0
        for permissao in permissoes:
            dados = (dados+1)
        print(dados)
        return dados

    def create_user(self, email, date_of_birth, password=None):

        # user = self.model(
        #     email=self.normalize_email(email),
        #     date_of_birth=date_of_birth,
        # )
        #
        # user.set_password(password)
        # user.save(using=self._db)
        # return user
        return 1

    def __str__(self):
        return self.first_name +' '+ self.last_name

class Laboratory(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    telefone = models.CharField(max_length=14)
    descricao = models.TextField()
    nome = models.CharField(max_length=30)
    atividades_realizadas = models.TextField()
    pesquisa_extensao = models.BooleanField()
    institution = models.ForeignKey(Institution, on_delete=models.PROTECT)
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
    institution = models.ForeignKey(Institution, on_delete=models.PROTECT)
    laboratory = models.ForeignKey(Laboratory, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nome

class Service(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    plataformas = models.TextField()
    descricao = models.TextField()
    nome = models.CharField(max_length=30)
    servidores = models.TextField()
    desenvolvedores = models.TextField()
    departamentos = models.TextField()
    institution = models.ForeignKey(Institution,  on_delete=models.SET_NULL, null=True)
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
        ('V', 'Vinculada'),
        ('B', 'FeedBack'),
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

class Demandcb(SafeDeleteModel):
    actions = (
        ('SER', 'Serviço'),
        ('LAB', 'Laboratorio'),
        ('EQU', 'Equipamento'),
    )

    demand = models.ForeignKey(Demand, on_delete=models.PROTECT)
    action = models.CharField(max_length=3, choices=actions, null=True)
    action_id = models.IntegerField(null=True)
    aceita_rejeita = models.BooleanField(null=True, default=None)

class DemandCallback(SafeDeleteModel):
    status = (
        ('S', 'Solicitado'),
        ('E', 'Analise'),
        ('R', 'Recusada'),
        ('A', 'Aceita'),
        ('P', 'Produção'),
        ('V', 'Vinculada'),
        ('B', 'FeedBack'),
        ('F', 'Finalizada'),
    )

    demand = models.ForeignKey(Demand, on_delete=models.CASCADE, default=None)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)
    status = models.CharField(choices=status, max_length=1, default='S')
    feedback = models.TextField()
    prazo_feedback = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Content(SafeDeleteModel):
    model = models.TextField()
    name = models.TextField()
    icon = models.TextField(default=None)

class Permission(SafeDeleteModel):

    permissions = (

        ('add_laboratory', 'Adicionar Laboratorio'),
        ('view_laboratory', 'Listar Laboratorio'),
        ('update_laboratory', 'Atualizar Laboratorio'),
        ('delete_laboratory', 'Deletar Laboratorio'),

        ('add_service', 'Adicionar Serviço'),
        ('view_service', 'Listar Serviço'),
        ('update_service', 'Atualizar Serviço'),
        ('delete_service', 'Deletar Serviço'),

        ('add_equipament', 'Adicionar Equipamento'),
        ('view_equipament', 'Listar Equipamento'),
        ('update_equipament', 'Atualizar Equipamento'),
        ('delete_equipament', 'Deletar Equipamento'),

        ('add_usuario', 'Adicionar Usuario'),
        ('view_usuario', 'Listar Usuario'),
        ('update_usuario', 'Atualizar Usuario'),
        ('delete_usuario', 'Deletar Usuario'),

        ('add_institution', 'Adicionar Instituição'),
        ('view_institution', 'Listar Instituição'),
        ('update_institution', 'Atualizar Instituição'),
        ('delete_institution', 'Deletar Instituição'),

        ('prospectar', 'Adicionar Instituição'),
        ('view_demand', 'Listar Instituição'),
        ('update_demand', 'Atualizar Instituição'),
        ('delete_demand', 'Deletar Instituição'),

        ('view_permission', 'Listar Instituição'),
        ('update_permission', 'Atualizar Instituição'),
        ('delete_institution', 'Deletar Instituição'),

    )

    name = models.TextField()
    content = models.ForeignKey(Content, on_delete=models.PROTECT)
    codigo = models.CharField(max_length=100 ,choices=permissions)

    class Meta:
        ordering = ['id']

class UserPermission(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

class UserContent(models.Model):
    profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)

class UserService(models.Model):
    profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

class Notification(SafeDeleteModel):

    titulo  = models.CharField(max_length=30)
    texto   = models.TextField()
    descricao   = models.TextField(null=True)
    icone   = models.CharField(max_length=30)
    ulr     = models.TextField()
    visualizada = models.BooleanField()
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    profile     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    def __str__(self):
        return self.titulo