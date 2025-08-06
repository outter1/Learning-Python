'''Crie uma função chamada ordenar_lista que recebe uma lista de numeros e retorna a lista ordenada em ordem crescente'''


def ordernar_lista(lista):
    if not lista:
        return []
    
    #ORDERNAR A LISTA
    lista_ordenada = sorted(lista)
    #lista_descrecente = sorted(lista, reverse=True)
    #sort deixa alinhado e sorted é uma lista
    
    print(f"Lista ordenada: {lista_ordenada}")

lista1 = [10, 2, 5, 9, 1, 0]
ordernar_lista(lista1)
    