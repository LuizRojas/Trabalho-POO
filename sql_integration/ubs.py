import sqlite3


con = sqlite3.connect("database.db")  # conectando com a base de dados

cur = con.cursor()  # criando cursor para operar funcionalidades do sql

######## CRIACAO DE TABELAS NO BANCO DE DADOS #########

cur.execute("CREATE TABLE IF NOT EXISTS UBS (nome TEXT, sigla TEXT)")

cur.execute("CREATE TABLE IF NOT EXISTS Servidor (nome TEXT, sigla TEXT)")

cur.execute("CREATE TABLE IF NOT EXISTS Vacinas (nome TEXT, fabricante TEXT, doenca TEXT)")

cur.execute("CREATE TABLE IF NOT EXISTS Lotes_vacinas (vacina TEXT, ubs TEXT, quantidade INTEGER, custo FLOAT, fonte TEXT)")

cur.execute("CREATE TABLE IF NOT EXISTS Agendamentos_vacinacao (ubs TEXT, vacina TEXT, nome TEXT, cpf INTEGER NOT NULL PRIMARY KEY)")

cur.execute("CREATE TABLE IF NOT EXISTS Vacinacoes_efetuadas (cpf INTEGER NOT NULL PRIMARY KEY)")

'''cur.execute("DELETE * FROM UBS")
cur.execute("DELETE * FROM Servidor")
cur.execute("DELETE * FROM Vacinas")
cur.execute("DELETE * FROM Lotes_vacinas")
cur.execute("DELETE * FROM Agendamentos_vacinacao")
cur.execute("DELETE * FROM Vacinacoes_efetuadas")'''


class UBS():
    def cadastrar_ubs(self, nome, sigla):
        cur.execute("INSERT INTO UBS (nome, sigla) values(?, ?)", (nome, sigla))
        con.commit()

    def cadastrar_servidor_municipal(self, nome, matricula, ubs: object):
        cur.execute("INSERT INTO Servidor (nome, matricula, ubs) values(?, ?, ?)", (nome, matricula, ubs))
        con.commit()

    def cadastrar_vacina(self, nome, fabricante, doenca):
        cur.execute("INSERT INTO Vacinas (nome, fabricante, doenca) values(?, ?, ?)", (nome, fabricante, doenca))
        con.commit()

    def receber_lote_vacina(self, vacina, ubs, qtd, custo, fonte):
        cur.execute("INSERT INTO Lotes_vacinas (vacina, ubs, quantidade, custo, fonte) values(?, ?, ?, ?, ?)", (vacina, ubs, qtd, custo, fonte))
        con.commit()

    def agendar_vacinacao(self, ubs, vacina, nome, cpf):
        cur.execute("INSERT INTO Agendamentos_vacinacao (ubs, vacina, nome, cpf) values(?, ?, ?, ?)", (ubs, vacina, nome, cpf))
        con.commit()
    
    def cancelar_agendamento_vacinacao(self, cpf):
        cur.execute("DELETE FROM Agendamentos_vacinacao WHERE cpf=?", (cpf))

    def registrar_vacinacao_efetuada(self, cpf):
        cur.execute("INSERT INTO Vacinacoes_efetuadas values(?)", (cpf))
    
    def exibir_dados(self, op=0):
        if (op == 0):
            res = cur.execute("SELECT * FROM sqlite_master")
            print(res.fetchall())

        if (op == 1):
            res = cur.execute("SELECT * FROM UBS")
            print(res.fetchall())

        if (op == 2):
            res = cur.execute("SELECT * FROM Servidor")
            print(res.fetchall())
        
        if (op == 3):
            res = cur.execute("SELECT * FROM Vacinas")
            print(res.fetchall())
        
        if (op == 4):
            res = cur.execute("SELECT * FROM Lotes_vacinas")
            print(res.fetchall())

        if (op == 5):
            res = cur.execute("SELECT * FROM Agendamentos")
            print(res.fetchall())

        if (op == 6):
            res = cur.execute("SELECT * FROM Vacinacoes_efetuadas")
            print(res.fetchall())
