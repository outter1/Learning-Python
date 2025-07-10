'''Ler 10 números e imprimir a soma, o maior e o menor'''
numeros = []

def ler_numeros():
    soma = 0
    maior = None
    menor = None #None means "nenhum valor definido"
    
    for i in range(10):
        num = float(input(f"Digite o (1 + 1)º numero:"))
        #range: gera uma sequência de numeros inteiros no intervalo
    
    soma += num
    
    if maior None or num > maior:
            maior = num
            
    if maior is None or num < menor:
            menor = num
            
    print(f"Soma dos numeros:  ")
    print(f"Maior número:  ") 
    print(f"Menor número:  ")  
    
    ler_numeros()   
