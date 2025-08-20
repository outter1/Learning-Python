#Lê o custo de fábrica
custo_fabrica = float(input("Digite o custo de fábrica do carro: R$ "))

#Define as porcentagens conforme a tabela
if custo_fabrica <= 12000:
    percentual_distribuidor = 5
    percentual_impostos = 0
elif custo_fabrica <= 25000:
    percentual_distribuidor = 10
    percentual_impostos = 15
else:
    percentual_distribuidor = 15
    percentual_impostos = 20

#Calcula os valores
comissao = custo_fabrica * (percentual_distribuidor / 100)
impostos = custo_fabrica * (percentual_impostos / 100)

#Calcula custo final
custo_consumidor = custo_fabrica + comissao + impostos

#Exibe o resultado
print(f"Custo ao consumidor: R$ {custo_consumidor:.2f}")