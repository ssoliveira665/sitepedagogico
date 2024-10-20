# Generated by Django 5.1.1 on 2024-10-20 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('capitulo', models.CharField(max_length=200)),
                ('tipo_alteracao', models.CharField(max_length=100)),
                ('justificativa', models.TextField()),
                ('nome_completo', models.CharField(max_length=200)),
                ('cpf', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=15)),
                ('cargo', models.CharField(max_length=100)),
                ('lotacao', models.CharField(max_length=100)),
                ('observacoes_adicionais', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('capitulo', models.CharField(max_length=255)),
                ('tipo_alteracao', models.CharField(choices=[('insercao', 'Inserção'), ('alteracao', 'Alteração'), ('supressao', 'Supressão'), ('exclusao', 'Exclusão')], max_length=100)),
                ('justificativa', models.TextField()),
                ('nome_completo', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.CharField(max_length=14)),
                ('telefone', models.CharField(max_length=15)),
                ('cargo', models.CharField(max_length=255)),
                ('lotacao', models.CharField(max_length=255)),
                ('observacoes_adicionais', models.TextField(blank=True, null=True)),
                ('data_submissao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
