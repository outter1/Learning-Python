nomeCompleto = input("Digite seu nome e sobrenome: ")

#versão original
print(nomeCompleto)

#Maiúsculas
print(nomeCompleto.upper())

#Minúculas
print(nomeCompleto.lower())

#Primeiro nome
nomes = nomeCompleto.split()
print(nomes[0], nomes[1])
