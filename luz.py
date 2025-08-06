'''Crie uma função estado_luz(status) que recebe uma string com o estado da luz: "Ligado", "desligado", "piscando".
Use match-case para retornar as seguintes mensagens:
"Luz ligada" para "on"
"Luz apagada" para "off"
"Luz piscando" para "Blink"
se for qualquer outro valor, "Estado desconhecido"
'''

def estado_luz(status):
    match status:
        case "Ligado":
            return "on"
        case "Desligado":
            return "off"
        case "Piscando":
            return "Blink"
        case _:
            return "Estado desconhecido"
        
num = input("Digite o status da sua lampada: ")
print(estado_luz(num))