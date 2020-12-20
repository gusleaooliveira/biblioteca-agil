from Banco import Banco 

class Livro:
    def __init__(self):
        self.banco = Banco("livro.db")
        self.banco.criarTabela("""
            CREATE TABLE IF NOT EXISTS livro(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome  TEXT,
                autor TEXT,
                ano TEXT,
                status TEXT
            )
        """)

    def inserir(self, nome, autor, ano, status):
        if ano.isdecimal() == True:
            sql="INSERT INTO livro (nome, autor, ano, status) VALUES (?,?,?,?)"
            lista=[nome, autor, int(ano), status]
            return self.banco.inserir(sql, lista)  
        else: 
            return False

    def selecionar(self):
        sql="SELECT * FROM livro"
        return self.banco.selecionar(sql)

    def selecionarNome(self, nome):
        sql="SELECT * FROM livro WHERE nome = ?"
        lista=(nome,)
        return self.banco.selecionarOpcao(sql, lista)

    def selecionarDisponivel(self, status="Disponível"):
        sql="SELECT * FROM livro WHERE status = ?"
        lista=(status,)
        return self.banco.selecionarOpcao(sql, lista)

    def selecionarIndisponivel(self, status="Indisponível"):
        sql="SELECT * FROM livro WHERE status = ?"
        lista=(status,)
        return self.banco.selecionarOpcao(sql, lista)

    def alterar(self, id, nome, autor, ano, status):
        if ano.isdecimal() == True:
            sql="UPDATE livro SET nome = ?, autor = ?, ano = ?, status = ? WHERE id = ?"
            lista=(nome, autor, int(ano), status, id)
            return self.banco.alterar(sql, lista)
        else:
            return False

    def statusLivro(self, id, status="Indisponível"):
        sql="UPDATE livro SET status = ? WHERE id = ?"
        lista=(status, id)
        return self.banco.alterar(sql, lista)

    def apagar(self, id):
        sql="DELETE FROM livro WHERE id = ?"
        lista=(id,)
        return self.banco.apagar(sql, lista)
        