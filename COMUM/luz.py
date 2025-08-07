def estado_luz(status):
    match status:
        case "ligada":
            return "on"
        case "desligada":
            return "off"
        case "piscando":
            return "blink"

        case _:
            return "Você ainda nem colocou a lâmpada"
            
resposta = input("Digite se a luz está ligada ou desligada ou piscando: ")
print(estado_luz(resposta))
