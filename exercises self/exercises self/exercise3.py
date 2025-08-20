'''3.	Implemente uma função que recebe uma lista de números e retorna True se todos eles forem positivos.'''
def momo(lista):
    return all(num > 0 for num in lista)

print(momo([1, 5, 2, -3, 1]))  