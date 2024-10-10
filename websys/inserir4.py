import os
import django

# Configurando o ambiente do Django para o script
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websys.settings')  # Substitua 'websys' pelo nome correto do seu projeto
django.setup()

from website.models import Disciplina  # Importando o modelo Disciplina

# Lista de disciplinas para cadastrar
disciplinas = [
    'Matemática',
    'Ciências',
    'Arte',
    'Educação Física',
    'História',
    'Geografia',
    'Inglês',
    'Redação'
]

# Função para cadastrar disciplinas no banco de dados
def cadastrar_disciplinas():
    for nome in disciplinas:
        disciplina, created = Disciplina.objects.get_or_create(nome=nome)
        if created:
            print(f"Disciplina '{nome}' cadastrada com sucesso.")
        else:
            print(f"Disciplina '{nome}' já existe no banco de dados.")

# Executando o cadastro das disciplinas
if __name__ == '__main__':
    cadastrar_disciplinas()
