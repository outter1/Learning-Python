def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        print("Impossivel dividir por zero")
    else:
        return a / b
    
    
def menu():
    print("Selecione a operação: ")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("0. Sair")
    opcao = input("Digite a opção: ")

    if opcao == '0':
        print("Saindo...")
    
    if opcao == '1':
        num1 = float(input("Digite o primeiro número:"))
        num2 = float(input("Digite o segundo número:"))
        print(f"Resultado: {soma(num1, num2)}")   #num1 é a primeira entrada e num2 é a segunda entrada
    elif opcao == '2':
        num1 = float(input("Digite o primeiro número:"))
        num2 = float(input("Digite o segundo número:")) 
        print(f"Resultado: {subtracao(num1, num2)}") 

    elif opcao == '3':
        num1 = float(input("Digite o primeiro número:"))
        num2 = float(input("Digite o segundo número:"))
        print(f"Resultado: {multiplicacao(num1, num2)}")
    elif opcao == '4':
        num1 = float(input("Digite o primeiro número:"))
        num2 = float(input("Digite o segundo número:"))
        resultado = divisao(num1, num2)
    
    else:
        print("Opção inválida. Tente novamente.")

while True:
    menu()
    if input("Deseja continuar? (s/n): ").lower() != 's':
        print("Saindo ...")
        break        
        