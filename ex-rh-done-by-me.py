'''Desenvolver um programa para ajudar o setor de RH a analisar os salários
dos colaboradores de empresa

Crie uma função chamada analisa_salarios() que receba uma quantidade variável de salários (números reais)
A função deve realizar as análises
*calcular a media salarial
*identificar o menor salário e o maior salário
*contar quantos colaboradores ganham acima da média salarial
*calcular o total pago em salários
'''

def analisa_salários(*salarios):
    
#Média salarial.    
    media = sum(salarios) / len(salarios)
#sum = soma
#len = le a quantidade de valores - se é 1 ou 2, 3, 4 e assim adiante

    maior = max(salarios)
    menor = min(salarios)  
#max = identifica o maior
#min = identifica o menor

#identifica quantos colaboradores ganham acima da média.
#A cada salário conte 1 se "S" for acima da média.
    high = sum(1 for s in salarios if s > media)
#A estrutura 1 for s in salarios if s > media gera 1 cada vez que o salário s é maior que a média
    
#Soma de todos      
    total = sum(salarios)
    
    return (
    f"A média salarial é de: {media:.2f}"
    f"O menor salário é de: {menor:.2f}"
    f"O maior salario é de: {maior:.2f}"
    f"A quantidade de colaboradores é de: {high}"
    f"O total pago em salários é: {total}"
    )
    
resultado = analisa_salários(1200, 1400, 1600, 1800)
print(resultado)