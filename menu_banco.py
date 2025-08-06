def menu(opcoes):
    match opcoes:
        case 0:
            return "Programa encerrado"
        case 1: 
            return "Seu saldo atual é: R$ 0,00"
        case 2:
            return float(input("Quanto deseja depositar: "))
        case 3: 
            return float(input("Quanto você deseja sacar: "))
        case _:
            return "Não existe essa opção"
        
option = int(input("Escolha uma opção: \n 0 - Sair\n 1 - Saldo\n 2 - Depositar\n 3 - Sacar"))
print(menu(option))        



    