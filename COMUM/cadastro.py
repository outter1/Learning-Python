funcionarios = []

while True:
    nome = input("Digite o nome do funcionário (ou 0 para encerrar): ")
    
    if nome == "0":
        break #parada


    #impedir que o usuário envie um campo vazio de funcionarios
    #strip remove espaços
    elif nome.strip() == "":
        print("Por favor insira um nome.")
        continue

    funcionarios.append(nome)

#\n é uma quebra de linha
print("\nLista de funcionários cadastrados: ")
for i, funcionario in enumerate(funcionarios, 1): #enumerate: itera sobre a sequência
#iterar = repetir
#enumerate(objeto a ser percorrido, valor inicial do indice)
    print(f"{i}. {funcionario}")