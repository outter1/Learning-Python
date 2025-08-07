#classe pai
class Carro:
    def __init__(self, motor, rodas):
        self.motor = motor
        self.rodas = rodas 
        
    def informação(self):
        return f"Carro com motor {self.motor} e {self.rodas}."
    
#classe que herda carro
class CarroEsportivo(Carro):
    def __init__(self, motor, rodas, turbo):
        super().__init__(motor, rodas) #chama o init de Carro
        self.turbo = turbo
        
    def ligar_turbo(self,):
        return f"Turbo Ligado!" if self.turbo else "Sem Turbo"

        
    def informação(self):
        return super().informação()
        return f"{base_informacao} Turbo: {"Sim" if self.turbo else "Não"}"
    
        
    #super(): usada para acessar método e propiedades da classe pai
    
carro1 = CarroEsportivo("Vá", 4, True)
print(carro1.informação())    
    
print(carro1.ligar_turbo())