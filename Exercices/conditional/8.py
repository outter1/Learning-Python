'''8.Leia a distância em km e a quantidade de litros de gasolina consumidos por um carro em um
percurso, calcule o consumo em km/l'''

km = float(input("Digite quantos km vc percorre: "))
gaso = float(input("Litros de gasolina "))

if km < 8:
    print("Venda o carro")

elif km > 8 and km < 14:
    print("Econômico")

else: 
    print("Super Econômico")

 
