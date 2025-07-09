def calculadora() :
    print("========BEM VINDO A CALCULADORA========")
    print("1. Soma \n2.Subtração \n3. Multiplicação \n4. Divisão ")
    opcao = int(input("Oque deseja fazer : "))
    numbone = float(input("Agora digite o primero número : "))
    numbtwo = float(input("Agora digite o segundo número : "))
    
    if opcao == 1 :
        print("A soma entre {} e {} é :".format(numbone, numbtwo))
        print(numbone + numbtwo)
        
    elif opcao == 2 :
        print("A subtração entre {} e {} é :".format(numbone, numbtwo))
        print(numbone - numbtwo)
        
    elif opcao == 3 : 
        print("A multiplicação entre {} e {} é :".format(numbone, numbtwo))
        print(numbone * numbtwo)
        
    elif opcao == 4 :
        print("A divisao entre {} e {} é :".format(numbone, numbtwo))
        print(numbone / numbtwo)
        
    else: 
        print("Opção inválida!") 
        
calculadora () 
        
    