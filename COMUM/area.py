def area_retangulo(largura, altura):
    area = largura * altura
    return area

largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))

print(f"A área do retângulo é: {area_retangulo(largura, altura)}")