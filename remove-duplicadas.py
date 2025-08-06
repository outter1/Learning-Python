'''Crie uma função chamada remover_duplicadas que recebe
uma lista e retorna uma nova lista sem elementos duplicados.'''

def remover_duplicadas(lista, lista2):
    nova_lista=[]
    vistos = set()
    
    for item in lista:
        if item not in vistos:
            nova_lista.append(item)
            vistos.add(item)
        return nova_lista
    
    lista = [1, 2, 2, 3, 4, 4, 5]
    resultado = remover_duplicadas(lista)
    print(resultado)
    