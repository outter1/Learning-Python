#Acessar elementos
vetor = ["a", "b", "c", 1, 2, 3]
primeiro = vetor[0] # "a"

#Fatiamento (slicing)
#Pega uma faixa de elementos
sub_vetor = vetor[1:4]
print(sub_vetor)

#Adicionar elementos
vetor.append("d") #Adiciona elemento ao final do vetor
print(vetor)

#Acionar vários elementos de uma vez
vetor.extend([4,5])

#Remover elementos
vetor.remove("b")

#Remover elemento ppor indice(posição)
del vetor[2]
#print(vetor)

frutas = ["mpango", "maçã", "Banana", "Pêra", "Kiwi", "Pitaya", "Jaca"]
frutas.pop(2)

#Atualizar elementos
#atribui um novo valor para a posição especíica
vetor[0] = "JLR"
print(vetor)

#len(IMPORTANTE)
tamanho_vetor = len(vetor)
print(tamanho_vetor)

#ordenação
matriculas = ["Reenam", "Gabriel", "Thais", "Breno"]
matriculas.sort()
print(matriculas)

#cria nova lista ordenada
novo_vetor = sorted(matriculas)
print(novo_vetor)

#Iteração : percorre os elementos
for estudante in matriculas:
    print(estudante)
    
#Dividir strings em palavras
frase = "Pyhon é muito bom!"
palavras = frase.split()
print(palavras)

#Juntar palavras em strings
nova_frase = " ".join(palavras)
print(nova_frase)

#Operaçõe matemáticas em vetores numericos
vetor_numerico = [1,2,3,4]
for i in range(len(vetor_numerico)):
    vetor_numerico[i] *=2 #vetor_numerico[i] = vetor_numerico[2] *2
print(vetor_numerico)


