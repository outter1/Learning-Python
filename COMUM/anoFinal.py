from datetime import datetime

nome = input("Por favor me diga qual é o seu nome: ")
idade = int(input("Por favor digite a sua idade: "))
anoAtual = datetime.now().year
anoDeNascimento = anoAtual - idade


print(f"Você terá 100 anos em: {anoDeNascimento + 100} ")