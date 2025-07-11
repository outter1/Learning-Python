pro = input("Digite o seu nome de usuário: ")
key = input("Digite a sua senha agora: ")

while pro == key:
    print("Não é aceito senha iguais a usuário")
    key = input("Digite sua senha novamente: ")
    
print("Sucess")