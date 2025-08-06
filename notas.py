'''Escreva uma função chamada classificar_nota
que recebe uma nota e retorna "Aprovado"m
"Reprovado" ou "Em Recuperação com base na nota.
'''


def classificar_nota(nota):
    if nota >= 7:
        print("Aprovado")
    
    elif nota >= 5 and nota < 7:
        print("Recuperação")
    
    elif nota > 100:
        print("Nota Inválida")
    
    elif nota > 5:
        print("Reprovado")
        
    else:
        print("Não foi possivel analisar a sua nota")
        
nota = float(input("Insira sua nota: "))
print(classificar_nota(nota))