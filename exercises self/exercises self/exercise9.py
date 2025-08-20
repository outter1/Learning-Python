class Jogador:
    def __init__(self, nome, pontos=0):
        self.nome = nome
        self.pontos = pontos

    def adicionar_pontos(self, pontos):
        self.pontos += pontos  # Atualiza os pontos do jogador
        return f"Pontos adicionados ao jogador {self.nome}: {self.pontos}"

    def zerar_pontos(self):
        self.pontos = 0  # Zera os pontos do jogador
        return f"O jogador {self.nome} teve os pontos zerados!\nPontos: {self.pontos}"

    def mostrar_pontos(self):
        return f"O jogador {self.nome} tem {self.pontos} pontos."  # Retorna os pontos do jogador


# Criação do jogador
nome = input("Digite o nome do seu jogador: ")
jogador1 = Jogador(nome)

# Adiciona pontos e exibe os resultados
print(jogador1.adicionar_pontos(1500))
print(jogador1.adicionar_pontos(1500))
print(jogador1.mostrar_pontos())