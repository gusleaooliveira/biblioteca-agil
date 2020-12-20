import sqlite3

class Banco:
    def conectar(self):
        self.conexao = sqlite3.connect(self.nome)
    
    def criarTabela(self, sql):
        cursor = self.conexao.cursor()
        cursor.execute(sql)
                
    def inserir(self, sql, valores):
        cursor = self.conexao.cursor()
        cursor.execute(sql, valores)
        self.conexao.commit()
        return True

    def selecionar(self, sql):
        cursor = self.conexao.cursor()
        cursor.execute(sql)
        itens = []
        for linha in cursor.fetchall():
            itens.append(linha)
        return itens

    def selecionarOpcao(self, sql, valores):
        cursor = self.conexao.cursor()
        cursor.execute(sql, valores)
        itens = []
        for linha in cursor.fetchall():
            itens.append(linha)
        return itens

    def alterar(self, sql, valores):
        cursor = self.conexao.cursor()
        cursor.execute(sql, valores)
        self.conexao.commit()
        return True

    def apagar(self, sql, valores):
        cursor = self.conexao.cursor()
        cursor.execute(sql, valores)
        self.conexao.commit()
        return True


    def __init__(self, nome):
        self.nome = nome
        self.conectar()

