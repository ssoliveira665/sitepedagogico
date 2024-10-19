from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings  # Para usar AUTH_USER_MODEL
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser

class Usuario(AbstractUser):
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)  # CPF único
    email = models.EmailField(unique=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_nascimento = models.DateField()  # Campo de data de nascimento
    telefone = models.CharField(max_length=15, null=True, blank=True)  # Telefone do Candidato
    telefone_contato_2 = models.CharField(max_length=15, null=True, blank=True)  # Telefone de Contato 2
    telefone_secundario = models.CharField(max_length=15, null=True, blank=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)  # Endereço
    bairro = models.CharField(max_length=100, null=True, blank=True)  # Bairro
    ponto_referencia = models.CharField(max_length=255, null=True, blank=True)  # Ponto de Referência
    maior_de_18 = models.BooleanField(default=False)  # O Candidato é maior de 18 anos?

    # New fields
    responsavel_legal = models.CharField(max_length=255, null=True, blank=True)
    tipo_responsavel = models.CharField(max_length=50, choices=[
        ('Mãe', 'Mãe'),
        ('Pai', 'Pai'),
        ('Responsável Legal', 'Responsável Legal')
    ], null=True, blank=True)

    # New field for special needs
    necessidade_especial = models.BooleanField(default=False)
    tipo_necessidade_especial = models.CharField(max_length=50, choices=[
        ('Baixa Visão', 'Baixa Visão'),
        ('Cegueira', 'Cegueira'),
        ('Auditiva', 'Auditiva'),
        ('Deficiência Física', 'Deficiência Física'),
        ('Deficiência Intelectual', 'Deficiência Intelectual')
    ], null=True, blank=True)

    # New field for Etapa da Matrícula
    etapa_matricula = models.CharField(max_length=50, choices=[
        ('Etapa I Ensino Fundamental I(1º 2º 3º ano)', 'Etapa I Ensino Fundamental I(1º 2º 3º ano)'),
        ('Etapa II Ensino Fundamental I(4º 5º ano)', 'Etapa II Ensino Fundamental I(4º 5º ano)'),
        ('Etapa III', 'Etapa III')
    ], null=True, blank=True)

    nome_responsavel = models.CharField(max_length=255, null=True, blank=True)  # Nome do Responsável Legal
    tipo_responsavel = models.CharField(max_length=50, choices=[('Mãe', 'Mãe'), ('Pai', 'Pai'), ('Responsável Legal', 'Responsável Legal')], null=True, blank=True)  # Tipo de Responsável Legal
    possui_necessidade_especial = models.BooleanField(default=False)  # Possui alguma necessidade especial?
    necessidade_especial_detalhe = models.CharField(
        max_length=50, 
        choices=[
            ('Baixa Visão', 'Baixa Visão'), 
            ('Cegueira', 'Cegueira'), 
            ('Auditiva', 'Auditiva'), 
            ('Deficiência Física', 'Deficiência Física'), 
            ('Deficiência Intelectual', 'Deficiência Intelectual')
        ],
        null=True, blank=True
    )  # Caso possua, favor assinalar
    turno_disponivel = models.CharField(
        max_length=20, 
        choices=[
            ('Manhã', 'Manhã'), 
            ('Tarde', 'Tarde'), 
            ('Noite', 'Noite')
        ],
        null=True, blank=True
    )  # Turno de Estudo Disponível
    etapa_pretendida = models.CharField(
        max_length=100,
        choices=[
            ('Etapa I Ensino Fundamental I (1º 2º 3º ano)', 'Etapa I Ensino Fundamental I (1º 2º 3º ano)'),
            ('Etapa II Ensino Fundamental I (4º 5º ano)', 'Etapa II Ensino Fundamental I (4º 5º ano)'),
            ('Etapa III Ensino Fundamental II', 'Etapa III Ensino Fundamental II')
        ],
        null=True, blank=True
    )  # Etapa pretendida para a matrícula
    
    # Related fields from AbstractUser
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_usuario_set',  # Name to avoid conflict
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_usuario_permissions_set',  # Name to avoid conflict
        blank=True
    )

    def __str__(self):
        return self.nome_completo
#**********************************************************************************************************
class Disciplina(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
#**********************************************************************************************************

class Inscricao(models.Model):
    candidato = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name="inscricao")
    data_inscricao = models.DateTimeField(auto_now_add=True)
    responsavel_legal = models.CharField(max_length=255, null=True, blank=True)
    tipo_responsavel = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    telefone_secundario = models.CharField(max_length=15, null=True, blank=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    bairro = models.ForeignKey('website.Bairro', on_delete=models.CASCADE)
    cidade = models.CharField(max_length=255, null=True, blank=True)  # Optional field
    ponto_referencia = models.CharField(max_length=255, null=True, blank=True)
    necessidade_especial = models.BooleanField(default=False)
    tipo_necessidade_especial = models.CharField(max_length=100, null=True, blank=True)
    turno_disponivel = models.CharField(max_length=100, null=True, blank=True)
    etapa_pretendida = models.CharField(max_length=255, null=True, blank=True)
    prova_realizada = models.BooleanField(default=False)  # Example field definition
    nota = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Add nota field
    aprovado = models.BooleanField(default=False)  # Add this field
    cpf_responsavel = models.CharField(max_length=11, null=True, blank=True)  # Novo campo
    rg_responsavel = models.CharField(max_length=12, null=True, blank=True)   # Novo campo
    disciplinas_aprovadas = models.ManyToManyField(Disciplina, related_name='inscricoes_aprovadas', blank=True)
    nota_prova = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Exemplo de campo de nota
    ativo = models.BooleanField(default=True)  # Define o status como ativo por padrão


    LOCAL_EXAME_CHOICES = [
        ('CMEJA', 'CMEJA Jose de Deus Andrade'),
        ('SEBASTIAO_AGRIPINO', 'EMEF Sebastião Agripino da Silva'),
        ('MARIA_LOURDES', 'EMEF Maria de Lourdes Rocha Rodrigues'),
        ('ADELAIDE_MOLINARI', 'EMEIF Adelaide Molinari'),
        ('RAIMUNDO_OLIVEIRA', 'EMEIF Raimundo de Oliveira'),
        ('TEOTONIO_VILELA', 'EMEIF Teotonio Vilela'),
    ]
    local_exame = models.CharField(max_length=30, choices=LOCAL_EXAME_CHOICES, default='CMEJA')

    ESCOLA_CHOICES = [
        ('NAO_ESTUDANDO', 'NÃO ESTOU ESTUDANDO EM 2024'),
        ('CMEJA_JOSE_DE_DEUS_ANDRADE', 'CMEJA JOSÉ DE DEUS ANDRADE'),
        ('EMEIF_ADELAIDE_MOLINARI', 'EMEIF ADELAIDE MOLINARI'),
        ('EMEIF_CARLOS_HENRIQUE', 'EMEIF CARLOS HENRIQUE'),
        ('EMEIF_JUSCELINO_KUBITSCHEK', 'EMEIF JUSCELINO KUBITSCHEK'),
        ('EMEIF_MAGALHAES_BARATA', 'EMEIF MAGALHÃES BARATA'),
        ('EMEIF_RAIMUNDO_OLIVEIRA', 'EMEIF RAIMUNDO DE OLIVEIRA'),
        ('EMEIF_TEOTONIO_VILELA', 'EMEIF TEOTÔNIO VILELA'),
        ('EMEF_BENEDITA_TORRES', 'EMEF BENEDITA TORRES'),
        ('EMEF_SEBASTIAO_AGRIPINO', 'EMEF SEBASTIÃO AGRIPINO DA SILVA'),
        ('EMEF_ALEXSANDRO_NUNES', 'EMEF ALEXSANDRO NUNES DE SOUZA GOMES'),
        ('EMEF_CARMELO_MENDES', 'EMEF CARMELO MENDES DA SILVA'),
        ('EMEB_LUIS_CARLOS_PRESTES', 'EMEB LUÍS CARLOS PRESTES'),
        ('EMEF_JOAO_NELSON', 'EMEF JOÃO NELSON DOS PRAZERES HENRIQUES'),
        ('EMEF_MARIA_DE_LOURDES', 'EMEF MARIA DE LOURDES ROCHA RODRIGUES'),
        ('EMEB_RONILTON_ARIDAL', 'EMEB RONILTON ARIDAL DA SILVA GRILO'),
        ('EMEB_GERCINO_CORREA', 'EMEB GERCINO CORREA'),
        ('EMEIF_TANCREDO', 'EMEIF TANCREDO DE ALMEIDA NEVES'),
        ('EMEIF_FRANCISCA_ROMANA', 'EMEIF FRANCISCA ROMANA'),
    ]

    local_exame = models.CharField(
        max_length=30,
        choices=LOCAL_EXAME_CHOICES,
        default='CMEJA',
        verbose_name='Local de realização das provas'
    )

    escola = models.CharField(
        max_length=50,
        choices=ESCOLA_CHOICES,
        default='NAO_ESTUDANDO',
        verbose_name='Nome da escola onde está matriculado em 2024'
    )

    dia_realizacao_prova = models.DateField(default='2024-12-01',verbose_name='Dia de realização da prova')

    # Field for "Deseja realizar a prova de todas as disciplinas?"
    PROVA_TODAS_DISCIPLINAS_CHOICES = [('Sim', 'Sim'),('Não', 'Não')]

    prova_todas_disciplinas = models.CharField(
        max_length=3,
        choices=PROVA_TODAS_DISCIPLINAS_CHOICES,
        default='Não',
        verbose_name="Deseja realizar a prova de todas as disciplinas?"
    )

    # Field for selected disciplines if "Não" is chosen
    DISCIPLINAS_CHOICES = [
        ('Matemática', 'Matemática'),
        ('Ciências', 'Ciências'),
        ('Arte', 'Arte'),
        ('Educação Física', 'Educação Física'),
        ('História', 'História'),
        ('Geografia', 'Geografia'),
        ('Língua Portuguesa', 'Língua Portuguesa'),
        ('Inglês', 'Inglês'),
    ]

    disciplinas = models.ManyToManyField(Disciplina, related_name='inscricoes_disciplinas', blank=True)

    EXAME_SUPLETIVO_CHOICES = [('Sim', 'Sim'),('Não', 'Não')]

    exame_supletivo = models.CharField(
        max_length=3, 
        choices=EXAME_SUPLETIVO_CHOICES,
        default='Não',  # Assuming 'Não' is the default choice
        verbose_name="Já fez a prova do exame supletivo anteriormente, ofertado pelo município de Canaã dos Carajás?"
    )

    # New Status Field
    STATUS_CHOICES = [('inscrito', 'Inscrito'),('approved', 'Aprovado'),('analise', 'Analise'),]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Inscrito')

    def __str__(self):
        return f"Inscrição de {self.candidato.nome_completo}"
    
    @property
    def formatted_id(self):
        return str(self.id).zfill(4)  # Isso vai adicionar zeros à esquerda até 4 dígitos

#**********************************************************************************************************

class Candidato(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    cpf = models.CharField(max_length=14)  # Add input mask for CPF in the form later
    data_nascimento = models.DateField()
    maior_de_18 = models.BooleanField()  # Yes or No (Checkbox)
    nome_responsavel = models.CharField(max_length=255, blank=True, null=True)
    
    TIPO_RESPONSAVEL_CHOICES = [
        ('mae', 'Mãe'),
        ('pai', 'Pai'),
        ('responsavel_legal', 'Responsável Legal'),
    ]
    tipo_responsavel = models.CharField(max_length=20, choices=TIPO_RESPONSAVEL_CHOICES, blank=True, null=True)
    
    telefone = models.CharField(max_length=15)
    telefone_2 = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)
    ponto_referencia = models.CharField(max_length=255, blank=True, null=True)
    
    possui_necessidade_especial = models.BooleanField()  # Checkbox for Yes or No
    
    NECESSIDADE_ESPECIAL_CHOICES = [
        ('baixa_visao', 'Baixa visão'),
        ('cegueira', 'Cegueira'),
        ('auditiva', 'Auditiva'),
        ('fisica', 'Deficiência Física'),
        ('intelectual', 'Deficiência Intelectual'),
    ]
    necessidade_especial = models.CharField(max_length=50, choices=NECESSIDADE_ESPECIAL_CHOICES, blank=True, null=True)

    TURNO_CHOICES = [
        ('manha', 'Manhã'),
        ('tarde', 'Tarde'),
        ('noite', 'Noite'),
    ]
    turno_disponivel = models.CharField(max_length=10, choices=TURNO_CHOICES)
    
    ETAPA_CHOICES = [
        ('etapa_i', 'Etapa I Ensino Fundamental I (1º 2º 3º ano)'),
        ('etapa_ii', 'Etapa II Ensino Fundamental I (4º 5º ano)'),
        ('etapa_iii', 'Etapa III Ensino Fundamental II'),
    ]
    etapa_pretendida = models.CharField(max_length=50, choices=ETAPA_CHOICES)

    def __str__(self):
        return self.nome
#**********************************************************************************************************

class School(models.Model):
    name = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    cep = models.CharField(max_length=10)  # Adding CEP field

    def __str__(self):
        return self.name
#**********************************************************************************************************
class Bairro(models.Model):
    logradouro_nome = models.CharField(max_length=255)
    bairro_distrito = models.CharField(max_length=255)
    cep = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.logradouro_nome} - {self.bairro_distrito}'
#**********************************************************************************************************

#**********************************************************************************************************
# class Disciplina(models.Model):
#     nome = models.CharField(max_length=100)

#     def __str__(self):
#         return self.nome
#**********************************************************************************************************
class Prova(models.Model):
    nome = models.CharField(max_length=255)
    data = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
#**********************************************************************************************************
class UserManager(BaseUserManager):
    def create_user(self, cpf, password=None, **extra_fields):
        if not cpf:
            raise ValueError("The CPF field is required")
        user = self.model(cpf=cpf, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, cpf, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(cpf, password, **extra_fields)
#**********************************************************************************************************

class User(AbstractBaseUser):
    cpf = models.CharField(max_length=11, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.cpf
#**********************************************************************************************************

class Funcionario(models.Model):
    nome_completo = models.CharField(max_length=255)
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=255)
    cargo = models.CharField(max_length=100)
    lotacao = models.CharField(max_length=100)  # Lotação refers to the work location or department

    def __str__(self):
        return self.nome_completo
#**********************************************************************************************************
class RegimentoCadastro(models.Model):
    TITULO_CHOICES = [
        ('TÍTULO I', 'TÍTULO I - DAS DISPOSIÇÕES PRELIMINARES'),
        ('TÍTULO II', 'TÍTULO II - DAS FINALIDADES E OBJETIVOS DA EDUCAÇÃO BÁSICA'),
        ('TÍTULO III', 'TÍTULO III - DA ORGANIZAÇÃO DA INSTITUIÇÃO'),
        ('TÍTULO IV', 'TÍTULO IV - DOS PAIS OU RESPONSÁVEIS'),
        ('TÍTULO V', 'TÍTULO V - DAS DEMAIS ORGANIZAÇÃO DA INSTITUIÇÃO'),
        ('TÍTULO VI', 'TÍTULO VI - DA ADMINISTRAÇÃO PESSOAL'),
        ('TÍTULO VII', 'TÍTULO VII - DA ORGANIZAÇÃO DIDÁTICA - PEDAGÓGICA'),
        ('TÍTULO VIII', 'TÍTULO VIII - DO REGIME DE FUNCIONAMENTO'),
        ('TÍTULO IX', 'TÍTULO IX - DA VERIFICAÇÃO DO RENDIMENTO E AVALIAÇÃO'),
        ('TÍTULO X', 'TÍTULO X - DO REGIME DISCIPLINAR'),
        ('TÍTULO XI', 'TÍTULO XI - DAS DISPOSIÇÕES GERAIS E TRANSITÓRIAS'),
        # Adicione os outros títulos conforme necessário
    ]
    
    TIPO_ALTERACAO_CHOICES = [
        ('supressao', 'Supressão'),
        ('insercao', 'Inserção'),
        ('edicao', 'Alteração'),
        ('exclusao', 'Exclusão'),
    ]
    
    titulo = models.CharField(max_length=255, choices=TITULO_CHOICES)
    capitulo = models.CharField(max_length=255)
    tipo_alteracao = models.CharField(max_length=50, choices=TIPO_ALTERACAO_CHOICES)
    justificativa = models.TextField()
    nome_completo = models.CharField(max_length=255)
    email = models.EmailField()
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    cargo = models.CharField(max_length=255, blank=True, null=True)
    lotacao = models.CharField(max_length=255, blank=True, null=True)
    observacoes_adicionais = models.TextField(blank=True, null=True)
    data_submissao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_completo