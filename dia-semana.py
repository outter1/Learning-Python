def dia_da_semana(dia):
    match dia:
        case "sábado" | "domingo":
            print("Fim de semana")
        case "segundo" | "terça" | "quarta" | "quinta" | "sexta":
            print("Dia útil")
            
        case _:
            print("Dia inválido!")
            
print(dia_da_semana("sábado"))
print(dia_da_semana("Kelly"))