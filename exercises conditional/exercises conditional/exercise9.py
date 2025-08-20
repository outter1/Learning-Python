def menu():
    print("100 - Cachorro quente")
    print("101 - Bauru Simples")
    print("102 -Bauru com Ovo") 
    print("103 - Hamburguer")
    print("104 - Cheeseamburguer")
    print("105 - Suco")
    print("106 - Refri")

    opcao = input("Opção escolhida: ")

    if opcao not in ("100", "101", "102", "103", "104", "105", "106"):
        print("Opção inválida")

    elif opcao == "100":
        print(f"Seu pedido custa: R$ 1,20")

    elif opcao == "101":
        print(f"Seu pedido custa: R$ 1,30")

    elif opcao == "102":
        print(f"Seu pedido custa: R$ 1,50")

    elif opcao == "103":
        print(f"Seu pedido custa: R$ 1,20")

    elif opcao == "104":
        print(f"Seu pedido custa: R$ 1,70")

    elif opcao == "105":
        print(f"Seu pedido custa: R$ 2,20")

    elif opcao == "106":
        print(f"Seu pedido custa: R$ 1,00")

    else:
        print("Erro")
    
menu()