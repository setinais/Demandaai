# Generated by Django 2.2.1 on 2019-05-21 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('nome', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=30)),
                ('icon', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('action', models.CharField(choices=[('SER', 'Serviços'), ('LAB', 'Laboratorios'), ('EQU', 'Equipamentos')], max_length=3)),
                ('action_id', models.IntegerField()),
                ('nome', models.CharField(max_length=30)),
                ('telefone', models.CharField(max_length=30)),
                ('codigo', models.CharField(max_length=9)),
                ('email', models.EmailField(max_length=40)),
                ('descricao', models.TextField()),
                ('cpf', models.CharField(max_length=20)),
                ('data_nascimento', models.DateField()),
                ('visualizada', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('nome', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('descricao', models.TextField()),
                ('phone', models.CharField(max_length=30)),
                ('site', models.CharField(max_length=60)),
                ('status', models.BooleanField()),
                ('street', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=11)),
                ('sector', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=30)),
                ('complement', models.CharField(max_length=60)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('nome', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('role', models.CharField(choices=[('AD', 'Administrador'), ('SE', 'Servidor'), ('PE', 'Proex'), ('DI', 'Diem'), ('PI', 'Propi'), ('TE', 'Técnico')], max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='users', to='demandai_administrador.Institution')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('plataformas', models.TextField()),
                ('descricao', models.TextField()),
                ('nome', models.CharField(max_length=30)),
                ('servidores', models.TextField()),
                ('desenvolvedores', models.TextField()),
                ('departamentos', models.TextField()),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('institution', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='services', to='demandai_administrador.Institution')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='services', to='demandai_administrador.User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('telefone', models.CharField(max_length=14)),
                ('descricao', models.TextField()),
                ('nome', models.CharField(max_length=30)),
                ('atividades_realizadas', models.TextField()),
                ('pesquisa_extensao', models.BooleanField()),
                ('endereco_sala', models.CharField(max_length=40)),
                ('servidores', models.TextField()),
                ('departamentos', models.TextField()),
                ('cursos', models.TextField()),
                ('status', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='laboratories', to='demandai_administrador.Institution')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='laboratories', to='demandai_administrador.User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('codigo', models.CharField(max_length=9)),
                ('descricao', models.TextField()),
                ('nome', models.CharField(max_length=30)),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='equipments', to='demandai_administrador.Institution')),
                ('laboratory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='equipments', to='demandai_administrador.Laboratory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='equipments', to='demandai_administrador.User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AccessControl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('create', models.BooleanField()),
                ('update', models.BooleanField()),
                ('delete', models.BooleanField()),
                ('select', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demandai_administrador.Action')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demandai_administrador.User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
