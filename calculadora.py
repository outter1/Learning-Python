print("Olá bem vindo a calculadora")
print("Escolha a operação matemática")

print("1 - Multiplicação")
print("2 - Divisão")
print("3 - Subtração")
print("4 - Adição")
escolha = input("Escolha de 1 a 4: ")

if escolha == "1":
    print("Você escolheu multiplicação")
    primeironumero = float(input("Digite o primeiro numero: "))
    segundonumero = float(input("Digite o segundo numero: "))
    print(f"O resultado foi de: {primeironumero * segundonumero}")
    
elif escolha == "2":
    print("Você escolheu divisão")
    print("Escolha os numeros")
    primeironumero = float(input("Selecione o primeiro numero: "))
    segundonumero = float(input("Digite o segundo numero: "))
    print(f"O resultado foi de: {primeironumero / segundonumero}")
    
elif escolha == "3":
    print("Você escolheu subtração")
    print("Escolha os numeros")
    primeironumero = float(input("Selecione o primeiro numero: "))
    segundonumero = float(input("Digite o segundo numero: "))
    print(f"O resultado foi de: {primeironumero - segundonumero}")
    
elif escolha == "4":
    print("Você escolheu adição")
    print("Escolha os numeros")
    primeironumero = float(input("Selecione o primeiro numero: "))
    segundonumero = float(input("Digite o segundo numero: "))
    print(f"O resultado foi de: {primeironumero + segundonumero}")
    
else:
    print("Opção Inválida")
    print("Selecione novamente")
    print("1 - Multiplicação")
    print("2 - Divisão")
    print("3 - Subtração")
    print("4 - Adição")
    escolha = input("Escolha de 1 a 4: ")
    
    