num = int(input("Digite um número: "))

if (num % 3 == 0) ^ (num % 5 == 0):
    print(f"O número {num} é divisível por 3 ou 5, mas não por ambos")
else:
    print(f"O número {num} não atenda à condição específico")
