import sqlite3

# Conectar ao banco de dados SQLite (db.sqlite3)
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Criar a tabela se ela não existir com os nomes de colunas corretos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS website_bairro (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        logradouro_nome TEXT NOT NULL,
        bairro_distrito TEXT NOT NULL,
        cep TEXT NOT NULL
    )
''')

# Lista de dados únicos a serem inseridos
dados = [
    ('Rua Amazonas', 'Alto Bonito I', '68354-115'),
    ('Rua Buriti', 'Alto Bonito II', '68352-021'),
    ('Rua Carajás', 'Alvorada I', '68350-237'),
    ('Rua Cinco', 'Alvorada II', '68350-249'),
    ('Avenida Pará', 'Bela Vista II', '68354-261'),
    ('Rua Arapoema', 'Bela Vista III', '68354-281'),
    ('Avenida Liberdade', 'Centro', '68350-073'),
    ('Rua Angelim', 'Cidade Nova I', '68354-611'),
    ('Rua V12', 'Estância Feliz I', '68350-263'),
    ('Rua Flamboyant', 'Estância Feliz II', '68350-281'),
    ('Rua Minas Gerais', 'Flor de Lis I', '68356-391'),
    ('Rua América', 'Flor de Lis II', '68356-407'),
    ('Avenida Pará', 'Jardim América', '68356-417'),
    ('Rua Cristal', 'Jardim das Palmeiras', '68352-145'),
    ('Avenida A', 'Jardim Europa I', '68356-479'),
    ('Avenida São João', 'Jardim Europa II', '68356-627'),
    ('Avenida Weyne Cavalcante', 'Jardim Florido', '68352-047'),
    ('Rua V12', 'Jardim Primavera', '68356-297'),
    ('Rua Airton Sena', 'João Pintinho', '68350-191'),
    ('Avenida Liberdade', 'Liberdade', '68350-121'),
    ('Rua Afonso Pena', 'Maranhense', '68350-107'),
    ('Rua Acapú', 'Mata da Serra', '68352-219'),
    ('Rua Afonso Pena', 'Monte Castelo', '68350-043'),
    ('Rua Amazonas', 'Montes Belos', '68352-083'),
    ('Rua da Torre', 'Montes Belos II', '68350-021'),
    ('Rua Tatajuba', 'Nova Canaã', '68356-045'),
    ('Avenida dos Pioneiros', 'Nova Canaã', '68356-007'),
    ('Rua Opala', 'Nova Canaã II', '68352-095'),
    ('Avenida Titânio', 'Nova Canaã II', '68352-087'),
    ('Rua Bahia', 'Novo Horizonte', '68356-169'),
    ('Avenida Anhanguera', 'Novo Horizonte II', '68356-213'),
    ('Rua América', 'Novo Horizonte III', '68356-257'),
    ('Avenida Weyne Cavalcante', 'Novo Brasil', '68354-532'),
    ('Rua Castelo Branco', 'Novo Paraiso', '68354-047'),
    ('Rua Aracajú', 'Parakanã', '68354-427'),
    ('Rua Airton Sena', 'Paraiso das Águas', '68354-229'),
    ('Rua das Violetas', 'Parque dos Ipês', '68356-075'),
    ('Avenida Pará', 'Park dos Carajás', '68354-215'),
    ('Avenida Weyne Cavalcante', 'Polo Industrial', '68350-341'),
    ('Rua Pastor Miguel', 'Portal do Sol', '68350-229'),
    ('Rua A', 'Ouro Preto', '68350-305'),
    ('Rua Arapoema', 'Oásis', '68354-237'),
    ('Rua A', 'Residencial Bela Vista', '68352-241'),
    ('Rua Arapoema', 'Residencial Jardim Bela Vista', '68354-267'),
    ('Rua Cristo Rei', 'Santa Vitória', '68356-351'),
    ('Rua Santa Catarina', 'Santana', '68354-521'),
    ('Avenida Liberdade', 'Esplanada', '68350-125'),
    ('Avenida Weyne Cavalcante', 'São José', '68350-141'),
    ('Rua Cristal', 'Serra Dourada III', '68352-201'),
    ('Avenida São João', 'Vale da Benção', '68350-351'),
    ('Rua Tocantins', 'Vale dos Sonhos I', '68350-371'),
    ('Rua A', 'Vale dos Sonhos II', '68350-411'),
    ('Rua Um', 'Vale dos Sonhos III', '68350-451'),
    ('Avenida Weyne Cavalcante', 'Vale Dourado', '68354-143'),
    ('Avenida Clarindo Morais da Silva', 'Vale Verde', '68354-053'),
    ('Rua Um', 'Vale dos Carajás', '68352-109'),
    ('Avenida Weyne Cavalcante', 'Vale do Sossego', '68350-313'),
    ('Rua Rio Branco', 'Via Oeste', '68354-461')
]


# Comando SQL para inserção usando os nomes de colunas corretos
try:
    cursor.executemany('''
        INSERT INTO website_bairro (logradouro_nome, bairro_distrito, cep) 
        VALUES (?, ?, ?)
    ''', dados)
    conn.commit()
    print("Dados inseridos com sucesso!")
except sqlite3.Error as error:
    print(f"Erro ao inserir os dados: {error}")
finally:
    # Fechar a conexão
    cursor.close()
    conn.close()
