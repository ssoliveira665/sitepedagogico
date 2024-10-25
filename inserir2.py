import sqlite3

# Connect to the SQLite database (db.sqlite3)
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Create the table if it doesn't exist with the correct column names
cursor.execute('''
    CREATE TABLE IF NOT EXISTS website_localprova (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        local_nome TEXT NOT NULL
    )
''')

# List of unique data to be inserted for local_nome
local_prova_data = [
    ('CMEJA Jose de Deus Andrade',),
    ('EMEF Sebastião Agripino da Silva',),
    ('EMEF Maria de Lourdes Rocha Rodrigues',),
    ('EMEIF Adelaide Molinari',),
    ('EMEIF Raimundo de Oliveira',),
    ('EMEIF Teotonio Vilela',),
    ('EMEB Gercino Correa de Melo Junior',)
]

# SQL command for inserting the data
try:
    cursor.executemany('''
        INSERT INTO website_localprova (local_nome) 
        VALUES (?)
    ''', local_prova_data)
    conn.commit()
    print("Data inserted successfully!")
except sqlite3.Error as error:
    print(f"Error inserting data: {error}")
finally:
    # Close the connection
    cursor.close()
    conn.close()
