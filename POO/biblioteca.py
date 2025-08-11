'''Crie um programa em Python que simule um sistema simples de biblioteca utilizando conceitos de Programação Orientada a Objetos (POO). O sistema deve:

Definir uma classe Livro que contenha, pelo menos, os atributos:

    titulo (nome do livro)

    autor (nome do autor)

Criar uma lista com pelo menos 10 objetos Livro, representando os livros disponíveis na biblioteca.

Solicitar ao usuário o nome do solicitante do empréstimo.

Exibir a lista de livros disponíveis, numerada para facilitar a seleção.

Pedir para o usuário escolher um número correspondente ao livro que deseja pegar emprestado.

Imprimir uma mensagem confirmando o empréstimo, informando o nome do solicitante e o livro selecionado (título e autor).'''
class Livro:
    def __init__ (self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def emprestimo(self):
        return "Livro comum emprestrado"

class Livro_de_terror(Livro):
    def __init__(self, titulo, autor, sangue):
        super().__init__(titulo, autor, sangue)
        self.sangue = sangue

    def emprestimo(self):
        if self.sangue:
            return "Livro de terror emprestado"
        else:
            return super().emprestimo()
        
class Livro_de_romance(Livro):
    def __init__(self, titulo, autor, love):
        super().__init__(titulo, autor, love)
        self.love = love

    def emprestimo(self):
        if self.love:
            return "Livro de romance emprestado"
        else:
            return super().emprestimo()
        
class Livro_de_acao(Livro):
    def __init__(self, titulo, autor, tiro):
        super().__init__(titulo, autor, tiro)
        self.tiro = tiro

    def emprestimo(self):
        if self.tiro:
            return "Livro de ação emprestado"
        else:
            return super().emprestimo()
        
class Livro_de_heroi(Livro):
    def __init__(self, titulo, autor, herois):
        super().__init__(titulo, autor, herois)
        self.herois = herois

    def emprestimo(self):
        if self.herois:
            return "Livro de heróis emprestado"
        else:
            return super().emprestimo()
        
class Livro_de_fada(Livro):
    def __init__(self, titulo, autor, fadas):
        super().__init__(titulo, autor, fadas)
        self.fadas = fadas

    def emprestimo(self):
        if self.fada:
            return "Livro de fada emprestado"
        else:
            return super().emprestimo()
        
class Livro_de_comedia(Livro):
    def __init__(self, titulo, autor, comedia):
        super().__init__(titulo, autor, comedia)
        self.comedia = comedia

    def emprestimo(self):
        if self.comedia:
            return "Livro de comedia emprestado"
        else:
            return super().emprestimo()
        
class Livro_de_criaca(Livro):
    def __init__(self, titulo, autor, desenhos):
        super().__init__(titulo, autor, desenhos)
        self.desenhos = desenhos

    def emprestimo(self):
        if self.desenhos:
            return "Livro de criança emprestado"
        else:
            return super().emprestimo()
        
class Livro_de_figurinhas(Livro):
    def __init__(self, titulo, autor, figuras):
        super().__init__(titulo, autor, figuras)
        self.figuras = figuras

    def emprestimo(self):
        if self.figuras:
            return "Livro de figurinhas emprestado"
        else:
            return super().emprestimo()
        
class Livro_de_estudos(Livro):
    def __init__(self, titulo, autor, exercicios):
        super().__init__(titulo, autor, exercicios)
        self.exercicios = exercicios

    def emprestimo(self):
        if self.exercicios:
            return "Livro de estudos emprestado"
        else:
            return super().emprestimo()
        
livro_normal = Livro("Normal", "Xucrut")
livro_terror = Livro_de_terror("Terror", "H.P Lovecraft")
livro_romance = Livro_de_romance("Romance", "Doug")
livro_acao = Livro_de_acao("Ação", "Leonardo")
livro_heroi = Livro_de_heroi("Herói", "Stan Lee")
livro_fada = Livro_de_fada("Fada", "Peter Pan")
livro_comedia = Livro_de_comedia("Comédia", "Adam Sandler")
livro_crianca = Livro_de_criaca("Doub", "Nano")
livro_estudos = Livro_de_estudos("Flake", "Threads")


#lista de polimorfismo
livros = [livro_normal, livro_terror, livro_romance, livro_acao, livro_heroi, livro_fada, livro_comedia, livro_crianca, livro_estudos]
for livro in livros:
    print(livro.emprestimo())
