import sqlite3

con = sqlite3.connect("hospitais.db")
cur = con.cursor()

cur.execute("SELECT COUNT(*) FROM hospitais")
total = cur.fetchone()[0]

print("Total de unidades:", total)

cur.execute("SELECT nome, tipo FROM hospitais LIMIT 10")
rows = cur.fetchall()

for r in rows:
    print(r)

con.close()