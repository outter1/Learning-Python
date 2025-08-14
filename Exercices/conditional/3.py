numero = int(input("Digite um número inteiro maior que zero: "))

if numero > 0:
    soma = 0
    for digito in str(numero):
        soma += int(digito)
    print("A soma dos dígitos é:", soma)
else:
    print("Número inválido")