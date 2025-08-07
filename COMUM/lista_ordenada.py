def ordenar_lista(lista):
    lista_ordenada = sorted(lista)
    return f"A ordem dos números é: {lista_ordenada}"

# Solicitando os números e convertendo para float
num1 = float(input("Escreva o primeiro número: "))
num2 = float(input("Escreva o segundo número: "))
num3 = float(input("Escreva o terceiro número: "))
num4 = float(input("Escreva o quarto número: "))

# Criando a lista de números
numeros = [num1, num2, num3, num4]

# Chamando a função
resultado = ordenar_lista(numeros)

# Exibindo o resultado
print(resultado)
