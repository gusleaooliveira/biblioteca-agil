import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Livro import Livro

class Janela:
    def apagar(self):
        self.limparItens()

        self.cb5 = QComboBox()

        lista=self.classLivro.selecionar()
        self.idItem=0
        for linha, item in enumerate(lista):
            for coluna, iten in enumerate(item):
                if coluna == 0:
                    self.idItem=iten
                if coluna == 1:
                    self.cb5.addItem(iten)
        
        self.btn = QPushButton("Apagar")
        self.btn.clicked.connect(self.apagarItem)

        self.grid.addWidget(QLabel("Livros:"), 0, 0)
        self.grid.addWidget(self.cb5, 0, 1)
        self.grid.addWidget(self.btn, 1, 0, 2, 2)

    def retirarLivro(self):
        self.limparItens()

        self.cb3= QComboBox()

        lista=self.classLivro.selecionarDisponivel()

        self.idItem = 0
        self.status = "Indisponível"

        for linha, item in enumerate(lista):
            for coluna, iten in enumerate(item):
                if coluna == 0:
                    self.idItem = iten
                if coluna == 1:
                    self.cb3.addItem(iten)
        
        self.enNome = QLineEdit()

        self.btn = QPushButton("Retirar")
        self.btn.clicked.connect(self.statusLivro)

        self.grid.addWidget(QLabel("Livros:"), 0, 0)
        self.grid.addWidget(self.cb3, 0, 1)
        self.grid.addWidget(QLabel("Nome do usuário:"), 1, 0)
        self.grid.addWidget(self.enNome, 1, 1)
        self.grid.addWidget(self.btn, 2, 0, 2, 2)

    def devolverLivro(self):
        self.limparItens()

        self.cb3= QComboBox()

        lista=self.classLivro.selecionarIndisponivel()

        self.idItem = 0
        self.status = "Disponível"

        for linha, item in enumerate(lista):
            for coluna, iten in enumerate(item):
                if coluna == 0:
                    self.idItem = iten
                if coluna == 1:
                    self.cb3.addItem(iten)
        

        self.btn = QPushButton("Devolver")
        self.btn.clicked.connect(self.statusLivro)

        self.grid.addWidget(QLabel("Livros:"), 0, 0)
        self.grid.addWidget(self.cb3, 0, 1)
        self.grid.addWidget(self.btn, 1, 0, 2, 2)

    def statusLivro(self):
        if self.enNome != None:
            val=self.classLivro.statusLivro(self.idItem, self.status, self.enNome.text())
        else:
            val=self.classLivro.statusLivro(self.idItem, self.status)
        if val == True:
            self.statusBar.showMessage(f"{self.status}!!", 2000)
        else:
            self.statusBar.showMessage(f"{self.status}!!", 2000)
        
        if self.status == "Indisponível":
            self.retirarLivro()
        elif self.status == "Disponível":
            self.devolverLivro()
            
    def selecionarItens(self, txt):
        lista=self.classLivro.selecionarNome(txt)
        self.idItem=0
        for i in lista:
            for cont,item in enumerate(i):
                if cont == 0:
                    self.idItem=item
                if cont == 1:
                    self.enNome.setText(item)
                if cont == 2:
                    self.enAutor.setText(item)
                if cont == 3:
                    self.enAno.setText(item)
                if cont == 4:
                    self.cb1.setCurrentText(item)

    def alterar(self):
        self.limparItens()

        self.cb = QComboBox()

        lista=self.classLivro.selecionar()
        
        for linha, item in enumerate(lista):
            for coluna, iten in enumerate(item):
                if coluna == 1:
                    self.cb.addItem(iten)
        
        self.cb.activated[str].connect(self.selecionarItens)
        
        self.enNome = QLineEdit()
        self.enAutor = QLineEdit()
        self.enAno = QLineEdit()
        self.cb1 = QComboBox()
        self.cb1.addItems(["Disponível", "Indisponível"])        

        self.btn = QPushButton("Alterar")
        self.btn.clicked.connect(self.alterarItem)

        self.grid.addWidget(QLabel("Livros:"), 0, 0)
        self.grid.addWidget(self.cb, 0, 1)
        self.grid.addWidget(QLabel("Nome do Livro:"), 1, 0)
        self.grid.addWidget(self.enNome, 1, 1)
        self.grid.addWidget(QLabel("Autor do Livro:"), 2, 0)
        self.grid.addWidget(self.enAutor, 2, 1)
        self.grid.addWidget(QLabel("Ano do Livro:"), 3, 0)
        self.grid.addWidget(self.enAno, 3, 1)
        self.grid.addWidget(QLabel("Ano do Livro:"), 4, 0)
        self.grid.addWidget(self.cb1, 4, 1)
        self.grid.addWidget(self.btn, 5, 0, 3, 3)

    def listar(self):
        self.limparItens()
        self.tabela = QTableWidget()

        lista=self.classLivro.selecionar()
        self.tabela.setRowCount(len(lista))
        self.tabela.setColumnCount(len(lista[0]))

        for linha, item in enumerate(lista):
            for coluna, iten in enumerate(item):
                if coluna % 4 == 0 and coluna != 0:
                    valor=''
                    if iten == True:
                        valor='Disponível'
                    else:
                        valor='Indisponível'
                    self.tabela.setItem(linha, coluna, QTableWidgetItem(valor))
                if coluna % 4 == 0 and coluna == 0:
                    self.tabela.setItem(linha, coluna, QTableWidgetItem(str(iten)))
                else:                
                    self.tabela.setItem(linha, coluna, QTableWidgetItem(iten))
                
           
        self.grid.addWidget(self.tabela, 0, 0)

    def apagarItem(self):
        val=self.classLivro.apagar(self.idItem)
        if val == True:
            self.statusBar.showMessage("Item apagado!!", 2000)
        else:
            self.statusBar.showMessage("Item não apagado!!", 2000)
        self.apagar()

    def cadastrarItem(self):
        val=self.classLivro.inserir(self.enNome.text(), self.enAutor.text(), self.enAno.text(), self.cb.currentText())
        if val == True:
            self.statusBar.showMessage("Item Cadastrado!!", 2000)
        else:
            self.statusBar.showMessage("Item não cadastrado!!", 2000)
        self.enNome.setText("")
        self.enAutor.setText("")
        self.enAno.setText("")
        self.cb.setCurrentText("Disponível")
    
    def alterarItem(self):
        val=self.classLivro.alterar(self.idItem, self.enNome.text(), self.enAutor.text(), self.enAno.text(), self.cb1.currentText())
        if val == True:
            self.statusBar.showMessage("Item alterar!!", 2000)
        else:
            self.statusBar.showMessage("Item não alterar!!", 2000)
        self.enNome.setText("")
        self.enAutor.setText("")
        self.enAno.setText("")
        self.cb1.setCurrentText("Disponível")

    def cadastrar(self):
        self.limparItens()
        
        self.enNome = QLineEdit()
        self.enAutor = QLineEdit()
        self.enAno = QLineEdit()
        self.cb = QComboBox()
        self.cb.addItems(["Disponível", "Indisponível"])        

        self.btn = QPushButton("Cadastrar")
        self.btn.clicked.connect(self.cadastrarItem)

        self.grid.addWidget(QLabel("Nome do Livro:"), 0, 0)
        self.grid.addWidget(self.enNome, 0, 1)
        self.grid.addWidget(QLabel("Autor do Livro:"), 1, 0)
        self.grid.addWidget(self.enAutor, 1, 1)
        self.grid.addWidget(QLabel("Ano do Livro:"), 2, 0)
        self.grid.addWidget(self.enAno, 2, 1)
        self.grid.addWidget(QLabel("Ano do Livro:"), 3, 0)
        self.grid.addWidget(self.cb, 3, 1)
        self.grid.addWidget(self.btn, 4, 0, 3, 3)
        

    def limparItens(self):
        for linha in range(0, self.grid.rowCount()):
            for coluna in range(0, self.grid.columnCount()):
                if self.grid.itemAtPosition(linha, coluna) != None: 
                    self.grid.itemAtPosition(linha, coluna).widget().setParent(None)
        

    def menu(self):
        self.barra = QMenuBar()
        self.livro = QMenu("Livro")
        self.biblioteca = QMenu("Livraria")

        self.bibliotecaDoarLivro = QAction("Doar Livro")
        self.bibliotecaDoarLivro.triggered.connect(self.cadastrar)
        self.bibliotecaRetirarLivro = QAction("Retirar Livro")
        self.bibliotecaRetirarLivro.triggered.connect(self.retirarLivro)
        self.bibliotecaDevolverLivro = QAction("Devolver Livro")
        self.bibliotecaDevolverLivro.triggered.connect(self.devolverLivro)
        

        self.livroCadastrar = QAction("Cadastrar")
        self.livroCadastrar.triggered.connect(self.cadastrar)
        self.livroListar = QAction("Listar")
        self.livroListar.triggered.connect(self.listar)
        self.livroAlterar = QAction("Alterar")
        self.livroAlterar.triggered.connect(self.alterar)
        self.livroApagar = QAction("Apagar")
        self.livroApagar.triggered.connect(self.apagar)
        
        self.livro.addAction(self.livroCadastrar)
        self.livro.addAction(self.livroListar)
        self.livro.addAction(self.livroAlterar)
        self.livro.addAction(self.livroApagar)
    
        self.biblioteca.addAction(self.bibliotecaDoarLivro)
        self.biblioteca.addAction(self.bibliotecaRetirarLivro)
        self.biblioteca.addAction(self.bibliotecaDevolverLivro)

        self.barra.addMenu(self.livro)
        self.barra.addMenu(self.biblioteca)

        self.janela.setMenuBar(self.barra) 
        
    def ui(self):
        self.grid = QGridLayout()
        self.statusBar = QStatusBar()
        self.widget.setLayout(self.grid)
        self.janela.setStatusBar(self.statusBar)

    def __init__(self):
        self.app = QApplication(sys.argv)

        self.widget = QWidget()

        self.janela = QMainWindow()
        self.janela.setWindowTitle("Biblioteca Ágil")
        self.janela.resize(800, 600)
        self.janela.show()
        self.janela.setCentralWidget(self.widget)

        
        
        self.ui()   
        self.classLivro = Livro()     
        self.menu()

        sys.exit(self.app.exec_())

if __name__ == '__main__':
    Janela()