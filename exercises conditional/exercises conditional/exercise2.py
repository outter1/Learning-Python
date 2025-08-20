h = float(input("Digite a sua altura: "))
sexo = input("Digite 'f' para feminino e 'm' para masculino: ")

peso_ideal_homem = (h * 72.7) - 58
peso_ideal_mulher = (h * 62.1) - 44.7

if sexo.lower() == "f":
    print(f"Seu peso ideal é: {peso_ideal_mulher:.2f}")
else:
    print(f"Seu peso ideal é: {peso_ideal_homem:.2f}")
