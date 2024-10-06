import sqlite3

# Connect to the SQLite database (db.sqlite3)
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Create the table if it doesn't exist with the correct column names
cursor.execute('''
    CREATE TABLE IF NOT EXISTS website_qualescola (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        escola_nome TEXT NOT NULL
    )
''')

# List of unique data to be inserted for escola_nome
escola_data = [
    ('NÃO ESTOU ESTUDANDO EM 2024',),
    ('CMEJA JOSÉ DE DEUS ANDRADE',),
    ('EMEIF ADELAIDE MOLINARI',),
    ('EMEIF CARLOS HENRIQUE',),
    ('EMEIF JUSCELINO KUBITSCHEK',),
    ('EMEIF MAGALHÃES BARATA',),
    ('EMEIF RAIMUNDO DE OLIVEIRA',),
    ('EMEIF TEOTÔNIO VILELA',),
    ('EMEF BENEDITA TORRES',),
    ('EMEF SEBASTIÃO AGRIPINO DA SILVA',),
    ('EMEF ALEXSANDRO NUNES DE SOUZA GOMES',),
    ('EMEF CARMELO MENDES DA SILVA',),
    ('EMEB LUÍS CARLOS PRESTES',),
    ('EMEF JOÃO NELSON DOS PRAZERES HENRIQUES',),
    ('EMEF MARIA DE LOURDES ROCHA RODRIGUES',),
    ('EMEB RONILTON ARIDAL DA SILVA GRILO',),
    ('EMEB GERCINO CORREA',),
    ('EMEIF TANCREDO DE ALMEIDA NEVES',),
    ('EMEIF FRANCISCA ROMANA',)
]

# SQL command for inserting the data
try:
    cursor.executemany('''
        INSERT INTO website_qualescola (escola_nome) 
        VALUES (?)
    ''', escola_data)
    conn.commit()
    print("Data inserted successfully!")
except sqlite3.Error as error:
    print(f"Error inserting data: {error}")
finally:
    # Close the connection
    cursor.close()
    conn.close()
