import pandas as pd
import sqlite3 as sq


con = sq.connect("database.db")

cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Alunos (nome TEXT, endereco INTEGER, matricula INTEGER NOT NULL PRIMARY KEY)")
cur.execute("INSERT INTO Alunos values('Reinaldo da Silva', 29122876, 1230009)")

df = pd.read_sql_table("SELECT * FROM Alunos", con)

print(df.head())

con.close()
