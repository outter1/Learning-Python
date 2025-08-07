class Carro:
    def __init__(self, motor, rodas):
        self.motor = motor
        self.rodas = rodas

    def acelerar(self):
        return "O carro está acelerando normalmente"
class CarroEsportivo(Carro):
    def __init__(self, motor, rodas, turbo):
        super().init(motor, rodas)
        self.turbo = turbo

    def acelerar(self):
        if self.turbo:
            return "O carro esportivo está acelerando com turbo! Vruum"
        else:
            return super().acelerar()
carro_normal = Carro("Veloster",4)
carro_esportivo_com_turbo = CarroEsportivo("Esportivo", 4, True)
carro_esportivo_sem_turbo = CarroEsportivo("Esportivo", 4, False)