salario = float(input("Insira seu salário atual: "))
pre = float("Quando você quer pagar de empréstimo: ")
if pre > 0.2 * salario:
    print("Emprestimo não concedido")
else:
    print("Emprestimo concedido")