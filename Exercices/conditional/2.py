h = float(input("Digite a sua altura atual: "))
sexo = input("Digite a seu sexo: ")

peso_ideal_h = (72,7 * h) - 58

peso_ideal_m = (62,1 * h) - 44.7

if sexo == h:
    print(f"Seu peso ideal é: {peso_ideal_h:2f}")

else: 
    print(f"Seu peso ideal é: {peso_ideal_m:.2f}")