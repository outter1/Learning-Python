'''1.	Escreva uma função que receba dois parâmetros: uma string e um caractere, e conte quantas vezes esse caractere aparece na string.'''

def contador(string, caractere):
    return string.count(caractere)
palavra = input("Digite uma palavra: ")

print(contador(palavra, "a"))