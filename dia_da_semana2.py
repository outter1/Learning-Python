'''Faça uma função dia_da_semana(numero) que recebe um numero de 1 a 7 e retorna o nome do dia da semana correspondente, sendo 1 para"Segunda-feira", 2 para "Terça -feira, 3 para
"Quarta-feira", 4 para "Quinta-feira", 5 para "Sexta-feira", 6 para "Sábado" e 7 para "Domingo"
'''

def dia_da_semana(dia_da_semana):
    match dia_da_semana:
        
        case 1:
            return "Segunda-Feira"
        case 2:
            return "Terça-feira"
        case 3:
            return "Quarta-feira"
        case 4:
            return "Quinta-feira"
        case 5:
            return "Sexta-feira"
        case 6:
            return "Sábado"
        case 7:
            return "Domingo"
        case _:
            return "Dia Inválido"
        
num = int(input("Digite um numero para saber dia da semana de 1 a 7: "))
print(dia_da_semana(num))