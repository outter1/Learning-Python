'''nome_dicionario = {chave1: valor1,
                   chave2: valor2,
                   chave3: valor3}'''

D = {"arroz": 30.00, "feijão": 9.00, "alcatra": 43.00, "alface": 3.00}
print(D)

print(D["alcatra"])

for chave, valor in D.items():
    print(f"Chave: {chave} | Valor: {valor}")