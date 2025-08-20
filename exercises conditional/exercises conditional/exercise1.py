salario = float(input("Digite o seu salário: "))
prestacao = float(input("Valor da prestação: "))
if prestacao > 0.2 * salario:
    print("Empréstimo não concedido")
else:
    print("Empréstimo concedido.")