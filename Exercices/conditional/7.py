print("Cálculos")
print("1 - Soma de 2 números")
print("2 - Diferença entre 2 números (maior pelo menor)")
print("3 - Produto entre 2 números")
print("4 - Divisão entre 2 números (o denominador não pode ser zero)")
opcao = input("Escolha de 1 a 4")


if opcao == 1:
    num1 = input("Digite o primeiro: ")
    num2 = input("Digite o segundo:")
    resultado = print(f"O resultado dessa soma é: {num1 + num2}")

elif opcao == 2:
    num1 = input("Digite o primeiro: ")
    num2 = input("Digite o segundo:")
    if num1 < num2:
        print(f"O resultado dessa soma é: {num1 - num2}")

elif opcao == 3:
    num1 = input("Digite o primeiro: ")
    num2 = input("Digite o segundo:")
    print(f"O resultado dessa divisão é: {num1 * num2}")

elif opcao == 4:
    num1 = input("Digite o primeiro: ")
    num2 = input("Digite o segundo:")
    if num1 or num2 != 0:
        print("Impossivel")
    else:
        print(f"O resultado dessa soma é: {num1 / num2}")

else:
    print("Nao deu fi")