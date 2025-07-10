'''Crie uma função que receba três numeros e mostre o maior deles.
'''

def mostra(a, b, c):
    if a >= b and a >= c:
        print(a)
    
    elif b >= a and b >= c:
        print(b)
    
    else:
        print(c)
    
mostra(1, 2, 3)