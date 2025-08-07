def menu(opcoes):
    match opcoes:
        case 0:
            return "Programa ecerrado"
        case 1:
            return "Seu saldo atual é: R$ 0,00"
        case 2:
            return float(input("Quanto deseja depositar: "))
        case 3:
            return float(input("Quanto deseja sacar: "))

        case _:
            return "Opção inválida."
            
resposta = int(input("Digite a operação que deseja\n 0 - Encerrar\n 1 - Saldo\n 2 - Depósito\n 3 - Saque: "))
print(menu(resposta))
