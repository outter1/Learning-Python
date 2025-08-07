#Criar vetor medicamentos
medicamentos = []

#Receber nome e preço de 15 medicamentos
for i in range(5):
    nome = input(f"Digite o nome do {i+1}º medicamento: ")
    preco_str = input(f"digite o preço do {i+1}º medicamento: R$ ")
    preco = float(preco_str.replace("," , ".")) 
    #replace: substitui a vírgula por ponto
    medicamentos.append({"nome": nome, "preço":preco}) 

#Informar o nome e o preço do medicamento mais barato
mais_barato = min(medicamentos, key=lambda x: x['preco'])
media = sum(medicamento["preco"] for medicamento in medicamentos)/5

print(f"\n Medicamento mais barato: {mais_barato["nome"]} ") 
#Funçao anônima: função sem nome --> lambda
#Lamda argumentos: expressão
#Argumentos = declarado na definição de uma função/método
#Argumento = valor real que fornece ao chamar a função 
#Média aritmética dos preços
print(f"\n Medicamento mais barato: {mais_barato[nome]} (R$) {mais_barato['preco']: 2f}")
print(f"Média aritmética dos preços: R$ {media: .2f}")