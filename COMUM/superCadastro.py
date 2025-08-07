nome = input("Digite seu nome: ")
idade = int(input("\nDigite sua idade: "))
salario = float(input("\nDigite seu salário: "))
genero = input("\nDigite 'm' para masculino| \n|'f' para feminino| \n|'o' outro|: ").lower()
estado_civil = input("\nDigite 's' para solteiro(a)| \n|'c' casado(a)| \n|'d' divorciado(a)| \n|'v' viúvo(a)|: ").lower()

while (len(nome) <= 3) or (idade < 0 or idade > 150) or (salario < 0) or (genero not in ("m", "f", "o")) or (estado_civil not in ("s", "c", "d", "v")):
    print("\nAlgumas informações estão incorretas, por favor preencha novamente.")
    nome = input("Digite seu nome: ")
    idade = int(input("\nDigite sua idade: "))
    salario = float(input("\nDigite seu salário: "))
    genero = input("\nDigite 'm' para masculino| \n|'f' para feminino| \n|'o' outro|: ").lower()
    estado_civil = input("\nDigite 's' para solteiro(a)| \n|'c' casado(a)| \n|'d' divorciado(a)| \n|'v' viúvo(a)|: ").lower()

if genero == "m":
    genero = "masculino"
elif genero == "f":
    genero = "feminino"
else:
    genero = "outro"

if estado_civil == "s":
    estado_civil = "solteiro(a)"
elif estado_civil == "c":
    estado_civil = "casado(a)"
elif estado_civil == "d":
    estado_civil = "divorciado(a)"
elif estado_civil == "v":
    estado_civil = "viúvo(a)"

print(f"\nNome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: {salario}")
print(f"Gênero: {genero}")
print(f"Estado civil: {estado_civil}")