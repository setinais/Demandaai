# Generated by Django 2.2.1 on 2019-12-05 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demandai_administrador', '0003_auto_20191205_1808'),
    ]

    operations = [
        migrations.AddField(
            model_name='demandcb',
            name='aceita_rejeita',
            field=models.BooleanField(default=None, null=True),
        ),
    ]