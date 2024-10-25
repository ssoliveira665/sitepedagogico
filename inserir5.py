import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('seu_banco_de_dados.db')
cursor = conn.cursor()

# Criar a tabela se ela ainda não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_completo TEXT NOT NULL,
    rg TEXT,
    cpf TEXT NOT NULL,
    telefone TEXT,
    email TEXT,
    cargo TEXT,
    lotacao TEXT
)
''')

# Dados que você deseja inserir (3 mil registros)
dados_funcionarios = [
    ('ANA CARLA DE SOUZA CASTRO SOUZA', '7121068', '03408633231', '(94)992537624', 'anacarla1923@hotmail.com', 'AGENTE DE SERVIÇOS ADMINISTRATIVOS - PCCR/QP', 'EMEF FRANCISCA ROMANA DOS SANTOS'),
    ('LIDIA MIRIAN RIBEIRO', '4656458', '00090892259', '94-91579084', 'LIDIA@ABAETETUBA.PA.BR', 'AGENTE DE SERVIÇOS DE BIBLIOTECA ESCOLAR - PCCR/QP', 'EMEF MARIA DE LOURDES ROCHA RODRIGUES'),
    ('SARA SIGNORELLI DE DEUS FREITAS', '4656458', '00090892259', '94-91579084', 'LIDIA@ABAETETUBA.PA.BR', 'AGENTE DE SERVIÇOS DE BIBLIOTECA ESCOLAR - PCCR/QP', 'EMEIF JUSCELINO KUBITSCHEK'),
    ('ELIANE BARBOSA DA SILVA', '3213065', '73145980297', None, 'SARA@ABAETETUBA.PA.BR', 'AUXILIAR DE SERVIÇOS GERAIS', 'EMEF SEBASTIÃO AGRIPINO DA SILVA'),
    ('WANDA DA SILVA DE OLIVEIRA', '5764713', '94757755287', '(94)992402524', 'elianebarbosa262524@gmail.com', 'SECRETÁRIO(A) ESCOLAR', 'EMEIF CARLOS HENRIQUE'),
    # Adicione os outros registros aqui ou carregue de um arquivo CSV/Excel
    # ...
]

# Inserir os dados em lote
cursor.executemany('''
INSERT INTO funcionarios (nome_completo, rg, cpf, telefone, email, cargo, lotacao)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', dados_funcionarios)

# Salvar (commit) as mudanças e fechar a conexão
conn.commit()
conn.close()

print("Dados inseridos com sucesso!")
