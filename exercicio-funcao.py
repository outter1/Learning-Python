'''Faça um programa que tenha função chamada maior(),
que rceba vários parâmetros com valores inteiros. Seu programa
tem que analisar todos os valores e dizer qual deles é o maior.
'''

def maior(a,b,c):
    if a > b and a > c:
        print(a)
    
    elif b > a and b > c:
        print(b)
    
    else:
        print(c)
        
num1 = int(input("First: "))
num2 = int(input("Second: "))
num3 = int(input("Third: "))

maior(num1,num2,num3)


'''Forma da Thaís'''

def maior(primeiro, *restantes):
    return max (primeiro, *restantes)

#Exemplos de uso:
#print(maior(10, 4,7 22, 13,17))
#print(maior(5, 5, 5))


