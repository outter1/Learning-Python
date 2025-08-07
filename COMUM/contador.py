soma = 0
contador = 1

while contador <= 5:
    numero = int(input(f"Digite o {contador}º número inteiro: "))
    soma += numero
    contador += 1
    
media = soma /5
print(f"Média aritmética: {media} ")