numero = int(input("Digite um número menor que 100: "))

if 0 <= numero < 100:
    dezena = numero // 10
    unidade = numero % 10

    soma = dezena + unidade

    print("A soma dos dígitos de {} é {}.".format(numero , soma))
else:
    print("Número inválido! Digite um número entre 0 e 99.") 
