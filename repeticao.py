
## WHILE ##
i = 1

while i <5:
    print(i) 
    i+=1 # i = i + 1 
'''While : usa quando quer repetir o código ENQUANTO a condição foi VERDADEIRA. 
Quando usar : Quando não se conhece o número previamente.
For : Quando se sabe o número de repetições ou quando iterar sobre uma sequência'''
alunos = ["Breno", "Gabriel", "Reenam"]


## FOR ##
'''
for aluno in alunos: # Para cada elemento in vetor
    print("Aluno : {}".format(aluno))  
# Para cada "aluno" , dentro de "alunos" faça:

frutas = ["Morango", "Banana", "Laranja"]

for fruta in frutas:
    print("Frutas : {}".format(fruta))
'''


numeros = int(input("Digite o número para ver a tabuada:"))
print("A tabuada do número : {}".format(numeros))
    
for i in range(1,11): # Range : Sequênciade números inteiros. range(inicio, parada)
    resultado = numeros * i
    print("{} X {} = {}".format(numeros, i, resultado)) 
