import sqlite3

con = sqlite3.connect("hospitais.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS hospitais (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    endereco TEXT,
    bairro TEXT,
    latitude REAL,
    longitude REAL,
    telefone TEXT,
    especialidades TEXT,
    tipo TEXT
)
""")

con.commit()
con.close()

print("Banco criado!")