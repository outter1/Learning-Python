class Cliente:
    def __init__(self):
        self.nome = None
        self.idade = None
        self.cpf = None

    def adicionando_cliente(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

# pedindo dados
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
cpf = input("Digite o seu cpf: ")

# criando cliente vazio e depois preenchendo
pessoa1 = Cliente()
pessoa1.adicionando_cliente(nome, idade, cpf)

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
cpf = input("Digite o seu cpf: ")

pessoa2 = Cliente()
pessoa2.adicionando_cliente(nome, idade, cpf)

print(f"Olá {pessoa1.nome}, cadastro concluído.... você tem {pessoa1.idade} anos, e seu cpf é {pessoa1.cpf}")
print(f"Olá {pessoa2.nome}, cadastro concluído.... você tem {pessoa2.idade} anos, e seu cpf é {pessoa2.cpf}")