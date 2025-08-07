def dia_da_semana(dia):
    match dia:
        case 1:
            return "segunda"
        case 2:
            return "terça"
        case 3:
            return "quarta"
        case 4:
            return "quinta"
        case 5:
            return "sexta"
        case 6:
            return "sábado"
        case 7:
            return "domingo"
        
        case _:
            return "Dia inválido!"
            
num = int(input("Digite o número referente ao dia da semana: "))
print(dia_da_semana(num))
