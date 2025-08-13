class Bike:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 60
    
    def ring_bell(self):
        print(f"A campainha da bicicleta {self.brand} {self.model} está tocando: TRING TRING!")
    
    def pedal(self, increment=5):
        self.speed += increment
        print(f"A bicicleta {self.brand} {self.model} está agora a {self.speed} km/h!")
        
    def brake(self, reduction=30):
        if self.speed - reduction > 50:
            self.speed = self.speed - reduction
        else:
            self.speed -= reduction
        print(f"A bicicleta {self.brand} {self.model} reduziu a velocidade para {self.speed} km/h!")
        
    def display_info(self):
        print(f"Bicicleta: {self.brand} {self.model}, Ano: {self.year}")
        
# Exemplo de uso
bike1 = Bike("Yamaha", "MT-07", 2021)
bike1.ring_bell()
bike1.pedal()
bike1.brake()
bike1.display_info()

