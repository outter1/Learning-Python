def analisa_salarios(*salarios):
    if not salarios:
        return "Nenhum salário foi fornecido"

    #Calcular a média salarial
    media_salarial = sum(salarios) / len(salarios)

    #Identificador do menor salário
    menor_salario = min(salarios)
    maior_salario = max(salarios)

    #Contar quantos colaboradores ganham acima da media salarial 
    acima_media = 0
    for salario in salarios:
        if salario > media_salarial:
            acima_media += 1
    #Total pago do salário

    total_pago = sum(salarios)

    #Retornar resultados
    return {
        "média_salarial" : media_salarial,
        "maior_salario" : maior_salario,
        "menor_salario" : menor_salario,
        "colaboradores_acima_media": acima_media,
        "total_pago" : total_pago
    }

print(analisa_salarios(1500,200,1800,3000,3500))