def analisa_salario(salarios):
    
    maior = max(salarios)
    menor = min(salarios)
    media = sum(salarios) / len(salarios)
    
    acima_media = 0
    for salario in salarios:
        if salario > media:
            acima_media += 1
    
    return (
        f"O maior salário é: {maior:.2f}\n"
        f"O menor salário é: {menor:.2f}\n"
        f"A média dos salários é: {media:.2f}\n"
        f"A quantidade de salários acima da média salarial é: {acima_media}"
    )
    
num1 = float(input("Escreva o primeiro é salário: "))
num2 = float(input("Escreva o segundo é salário: "))
num3 = float(input("Escreva o terceiro é salário: "))
num4 = float(input("Escreva o quarto é salário: "))

resultado = analisa_salario((num1, num2, num3, num4))    
print(resultado)