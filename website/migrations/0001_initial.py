# Generated by Django 5.1.1 on 2024-10-19 13:25

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro_nome', models.CharField(max_length=255)),
                ('bairro_distrito', models.CharField(max_length=255)),
                ('cep', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.CharField(max_length=14)),
                ('data_nascimento', models.DateField()),
                ('maior_de_18', models.BooleanField()),
                ('nome_responsavel', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_responsavel', models.CharField(blank=True, choices=[('mae', 'Mãe'), ('pai', 'Pai'), ('responsavel_legal', 'Responsável Legal')], max_length=20, null=True)),
                ('telefone', models.CharField(max_length=15)),
                ('telefone_2', models.CharField(blank=True, max_length=15, null=True)),
                ('endereco', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=100)),
                ('ponto_referencia', models.CharField(blank=True, max_length=255, null=True)),
                ('possui_necessidade_especial', models.BooleanField()),
                ('necessidade_especial', models.CharField(blank=True, choices=[('baixa_visao', 'Baixa visão'), ('cegueira', 'Cegueira'), ('auditiva', 'Auditiva'), ('fisica', 'Deficiência Física'), ('intelectual', 'Deficiência Intelectual')], max_length=50, null=True)),
                ('turno_disponivel', models.CharField(choices=[('manha', 'Manhã'), ('tarde', 'Tarde'), ('noite', 'Noite')], max_length=10)),
                ('etapa_pretendida', models.CharField(choices=[('etapa_i', 'Etapa I Ensino Fundamental I (1º 2º 3º ano)'), ('etapa_ii', 'Etapa II Ensino Fundamental I (4º 5º ano)'), ('etapa_iii', 'Etapa III Ensino Fundamental II')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=255)),
                ('rg', models.CharField(max_length=20)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=255)),
                ('cargo', models.CharField(max_length=100)),
                ('lotacao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Prova',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('data', models.DateField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RegimentoCadastro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('capitulo', models.CharField(max_length=255)),
                ('tipo_alteracao', models.CharField(max_length=50)),
                ('justificativa', models.TextField()),
                ('nome_completo', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.CharField(max_length=14)),
                ('telefone', models.CharField(max_length=20)),
                ('cargo', models.CharField(max_length=255)),
                ('lotacao', models.CharField(max_length=255)),
                ('observacoes_adicionais', models.TextField(blank=True, null=True)),
                ('data_submissao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('neighborhood', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('cep', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nome_completo', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_nascimento', models.DateField()),
                ('telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('telefone_contato_2', models.CharField(blank=True, max_length=15, null=True)),
                ('telefone_secundario', models.CharField(blank=True, max_length=15, null=True)),
                ('endereco', models.CharField(blank=True, max_length=255, null=True)),
                ('bairro', models.CharField(blank=True, max_length=100, null=True)),
                ('ponto_referencia', models.CharField(blank=True, max_length=255, null=True)),
                ('maior_de_18', models.BooleanField(default=False)),
                ('responsavel_legal', models.CharField(blank=True, max_length=255, null=True)),
                ('necessidade_especial', models.BooleanField(default=False)),
                ('tipo_necessidade_especial', models.CharField(blank=True, choices=[('Baixa Visão', 'Baixa Visão'), ('Cegueira', 'Cegueira'), ('Auditiva', 'Auditiva'), ('Deficiência Física', 'Deficiência Física'), ('Deficiência Intelectual', 'Deficiência Intelectual')], max_length=50, null=True)),
                ('etapa_matricula', models.CharField(blank=True, choices=[('Etapa I Ensino Fundamental I(1º 2º 3º ano)', 'Etapa I Ensino Fundamental I(1º 2º 3º ano)'), ('Etapa II Ensino Fundamental I(4º 5º ano)', 'Etapa II Ensino Fundamental I(4º 5º ano)'), ('Etapa III', 'Etapa III')], max_length=50, null=True)),
                ('nome_responsavel', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_responsavel', models.CharField(blank=True, choices=[('Mãe', 'Mãe'), ('Pai', 'Pai'), ('Responsável Legal', 'Responsável Legal')], max_length=50, null=True)),
                ('possui_necessidade_especial', models.BooleanField(default=False)),
                ('necessidade_especial_detalhe', models.CharField(blank=True, choices=[('Baixa Visão', 'Baixa Visão'), ('Cegueira', 'Cegueira'), ('Auditiva', 'Auditiva'), ('Deficiência Física', 'Deficiência Física'), ('Deficiência Intelectual', 'Deficiência Intelectual')], max_length=50, null=True)),
                ('turno_disponivel', models.CharField(blank=True, choices=[('Manhã', 'Manhã'), ('Tarde', 'Tarde'), ('Noite', 'Noite')], max_length=20, null=True)),
                ('etapa_pretendida', models.CharField(blank=True, choices=[('Etapa I Ensino Fundamental I (1º 2º 3º ano)', 'Etapa I Ensino Fundamental I (1º 2º 3º ano)'), ('Etapa II Ensino Fundamental I (4º 5º ano)', 'Etapa II Ensino Fundamental I (4º 5º ano)'), ('Etapa III Ensino Fundamental II', 'Etapa III Ensino Fundamental II')], max_length=100, null=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='custom_usuario_set', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='custom_usuario_permissions_set', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inscricao', models.DateTimeField(auto_now_add=True)),
                ('responsavel_legal', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_responsavel', models.CharField(blank=True, max_length=100, null=True)),
                ('telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('telefone_secundario', models.CharField(blank=True, max_length=15, null=True)),
                ('endereco', models.CharField(blank=True, max_length=255, null=True)),
                ('cidade', models.CharField(blank=True, max_length=255, null=True)),
                ('ponto_referencia', models.CharField(blank=True, max_length=255, null=True)),
                ('necessidade_especial', models.BooleanField(default=False)),
                ('tipo_necessidade_especial', models.CharField(blank=True, max_length=100, null=True)),
                ('turno_disponivel', models.CharField(blank=True, max_length=100, null=True)),
                ('etapa_pretendida', models.CharField(blank=True, max_length=255, null=True)),
                ('prova_realizada', models.BooleanField(default=False)),
                ('nota', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('aprovado', models.BooleanField(default=False)),
                ('cpf_responsavel', models.CharField(blank=True, max_length=11, null=True)),
                ('rg_responsavel', models.CharField(blank=True, max_length=12, null=True)),
                ('nota_prova', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('ativo', models.BooleanField(default=True)),
                ('local_exame', models.CharField(choices=[('CMEJA', 'CMEJA Jose de Deus Andrade'), ('SEBASTIAO_AGRIPINO', 'EMEF Sebastião Agripino da Silva'), ('MARIA_LOURDES', 'EMEF Maria de Lourdes Rocha Rodrigues'), ('ADELAIDE_MOLINARI', 'EMEIF Adelaide Molinari'), ('RAIMUNDO_OLIVEIRA', 'EMEIF Raimundo de Oliveira'), ('TEOTONIO_VILELA', 'EMEIF Teotonio Vilela')], default='CMEJA', max_length=30, verbose_name='Local de realização das provas')),
                ('escola', models.CharField(choices=[('NAO_ESTUDANDO', 'NÃO ESTOU ESTUDANDO EM 2024'), ('CMEJA_JOSE_DE_DEUS_ANDRADE', 'CMEJA JOSÉ DE DEUS ANDRADE'), ('EMEIF_ADELAIDE_MOLINARI', 'EMEIF ADELAIDE MOLINARI'), ('EMEIF_CARLOS_HENRIQUE', 'EMEIF CARLOS HENRIQUE'), ('EMEIF_JUSCELINO_KUBITSCHEK', 'EMEIF JUSCELINO KUBITSCHEK'), ('EMEIF_MAGALHAES_BARATA', 'EMEIF MAGALHÃES BARATA'), ('EMEIF_RAIMUNDO_OLIVEIRA', 'EMEIF RAIMUNDO DE OLIVEIRA'), ('EMEIF_TEOTONIO_VILELA', 'EMEIF TEOTÔNIO VILELA'), ('EMEF_BENEDITA_TORRES', 'EMEF BENEDITA TORRES'), ('EMEF_SEBASTIAO_AGRIPINO', 'EMEF SEBASTIÃO AGRIPINO DA SILVA'), ('EMEF_ALEXSANDRO_NUNES', 'EMEF ALEXSANDRO NUNES DE SOUZA GOMES'), ('EMEF_CARMELO_MENDES', 'EMEF CARMELO MENDES DA SILVA'), ('EMEB_LUIS_CARLOS_PRESTES', 'EMEB LUÍS CARLOS PRESTES'), ('EMEF_JOAO_NELSON', 'EMEF JOÃO NELSON DOS PRAZERES HENRIQUES'), ('EMEF_MARIA_DE_LOURDES', 'EMEF MARIA DE LOURDES ROCHA RODRIGUES'), ('EMEB_RONILTON_ARIDAL', 'EMEB RONILTON ARIDAL DA SILVA GRILO'), ('EMEB_GERCINO_CORREA', 'EMEB GERCINO CORREA'), ('EMEIF_TANCREDO', 'EMEIF TANCREDO DE ALMEIDA NEVES'), ('EMEIF_FRANCISCA_ROMANA', 'EMEIF FRANCISCA ROMANA')], default='NAO_ESTUDANDO', max_length=50, verbose_name='Nome da escola onde está matriculado em 2024')),
                ('dia_realizacao_prova', models.DateField(default='2024-12-01', verbose_name='Dia de realização da prova')),
                ('prova_todas_disciplinas', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], default='Não', max_length=3, verbose_name='Deseja realizar a prova de todas as disciplinas?')),
                ('exame_supletivo', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], default='Não', max_length=3, verbose_name='Já fez a prova do exame supletivo anteriormente, ofertado pelo município de Canaã dos Carajás?')),
                ('status', models.CharField(choices=[('inscrito', 'Inscrito'), ('approved', 'Aprovado'), ('analise', 'Analise')], default='Inscrito', max_length=20)),
                ('bairro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.bairro')),
                ('candidato', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='inscricao', to=settings.AUTH_USER_MODEL)),
                ('disciplinas', models.ManyToManyField(blank=True, related_name='inscricoes_disciplinas', to='website.disciplina')),
                ('disciplinas_aprovadas', models.ManyToManyField(blank=True, related_name='inscricoes_aprovadas', to='website.disciplina')),
            ],
        ),
    ]
