print("Validador de Informações")

nome = input("Insira seu nome: ")
idade = int(input("Insira sua idade: "))
salario = float(input("Insira seu salário"))
genero = (input("Insira seu gênero: "))
estadocivil = (input("Insira seu estado civil - \nS: solteiro(a) | \nC: para cadado(a) | \nV: para víuvo | \nD: para divorciado|:  "))

while True:
    if len(nome) <= 3 or idade < 0 or salario < 0: 
        print("Informações incorretas")
        print("Tente novamente!")
        nome = input("Insira seu nome: ")
        idade = int(input("Insira sua idade: "))
        salario = float(input("Insira seu salário"))
        genero = (input("Insira seu gênero: "))
        estadocivil = (input("Insira seu estado civil - \nS: solteiro(a) | \nC: para cadado(a) | \nV: para víuvo | \nD: para divorciado|:  "))
        
        
        if genero == "f" or "F":
            print("Feminino")
            
        if genero == "M" or "m":
            print("Masculino")
            
        if genero == "O" or "o":
            print("Outro")
    
    print("Cadastro Concluido")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Salário: {salario}")
    print(f"Genero: {genero}")
    print(f"Estado Civil: {estadocivil}")
    
    break