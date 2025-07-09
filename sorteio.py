from random import choice
num = [0,1,2,3,4,5]
numero = choice(num) 
print("=======JOGO DE ADIVINHAÇÃO=======")
print("Tente adivinha o número que eu escolhi!")
escolha = int(input("Escolha um número de 0 a 5 : "))
if escolha == numero:
    print("O número que você escolheu foi : {}".format(escolha))
    print("O número sorteado foi : {}".format(numero))
    print("Parabéns! Você ganhou!")
elif escolha > 5:
    print("Número inválido. Escolha um número de 0 a 5")
else:
    print("O número escolhido foi : {}".format(escolha))
    print("O número sorteado foi : {}".format(numero)) 
    print("Você perdeu!")  