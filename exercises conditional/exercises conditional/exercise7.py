def menu():
    print("1 - Soma de 2 números")
    print("2 - Diferença entre 2 números (maior pelo menor)")
    print("3 - Produto entre 2 números") 
    print("4 - Divisão entre 2 números (o denominador não pode ser zero)")
    opcao = input("Opção escolhida: ")

    if opcao not in ("1", "2", "3", "4"):
        print("Opção inválida")

    elif opcao == "1":
        num1 = float(input("Digite o primeiro o número: "))
        num2 = float(input("Digite o segundo o número: "))
        print(f"Sua soma é: {num1 + num2}")

    elif opcao == "2":
        num1 = float(input("Digite o primeiro o número: "))
        num2 = float(input("Digite o segundo o número: "))
        if num1 < num2:
            print(f"Sua subtração é: {num2 - num1}")
        else:
            print(f"Sua subtração é: {num1 - num2}")

    elif opcao == "3":
        num1 = float(input("Digite o primeiro o número: "))
        num2 = float(input("Digite o segundo o número: "))
        print(f"Sua multiplicação é: {num1 * num2}")

    elif opcao == "4":
        num1 = float(input("Digite o primeiro o número: "))
        num2 = float(input("Digite o segundo o número: "))
        if num2 == 0:
            print("Sua divisão é impossível")
        else:
            print(f"Sua divisão é: {num1 / num2}")

    else:
        print("Erro")
    
menu()