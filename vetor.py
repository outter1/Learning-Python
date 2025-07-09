# Acessar elemntos 
vetor = ["a", "b", "c", 1, 2, 3]
primeiro = vetor[0] #"a" 
print(primeiro) 

#Fatiamento (slicing)
#Pega uma faixa de elementos
sub_vetor = vetor[1:4]
print(sub_vetor)

#Adicionar elementos
vetor.append("d")#Adicionar elemento ao final de setor 
print(vetor)

#Adicionar vários elementos de uma vez
vetor.extend([4, 5])

#Remover elementos
vetor.remove("b") 

del vetor[2]  
#print(vetor)

frutas = ["Morango", "Maçã", "Banana"] # Pop é para eliminar pelo número do vetor
frutas.pop(2)
print(frutas)

#Atualizar elementos
#Atribui um novo valor para a posição específica
vetor[0] = "JRL"
print(vetor) 


#Len (Importante)
tamanho_vetor = len(vetor)
print(vetor)
print(tamanho_vetor)

#Ordenação
matriculas = ["Gabriel", "Breno", "Nicolly", "Antonio", "Matheus"]
matriculas.sort()
print(matriculas) 

#Criar nova lista ordenada
novo_vetor = sorted(matriculas)
print(novo_vetor)

#itineração : Pecorre os elementos
for estudante in matriculas:
    print(estudante) 
    
# Dividir strings em palavras 
frase = "Python é muito bom!"
palavras = frase.split()
print(palavras) 

#Juntar palavras em string 
nova_frase = "Nova frase".join(palavras)


#Operações matemáticas em vetores numéricos
vetor_numerico = [1,2,3,4]
for i in range(len(vetor)):
    vetor[i]*=2
print(vetor_numerico)