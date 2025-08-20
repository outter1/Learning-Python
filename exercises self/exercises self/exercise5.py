'''5.	Crie uma classe Elevador com atributos para andar atual, total de andares e capacidade. Implemente métodos para subir e descer andares.'''
class Elevador:
    def __init__(self, andar_atual, total_andares, capacidade):
        self.andar_atual = andar_atual
        self.total_andares = total_andares
        self.capacidade = capacidade

    def subir(self):
        if self.andar_atual < self.total_andares:
            self.andar_atual += 1
            print(f"Subiu para o andar {self.andar_atual}")
        else:
            print("Já está no último andar.")

    def descer(self):
        if self.andar_atual > 0:
            self.andar_atual -= 1
            print(f"Desceu para o andar {self.andar_atual}")
        else:
            print("Já está no térreo.")

    def atual(self):
        return self.andar_atual

# Exemplo de uso:
elevador = Elevador(0, 5, 8)  # Começa no térreo, 5 andares, capacidade 8 pessoas
elevador.subir()  # Subiu para o andar 1
elevador.subir()  # Subiu para o andar 2
elevador.descer() # Desceu para o andar 1
print(elevador.atual())  # 1