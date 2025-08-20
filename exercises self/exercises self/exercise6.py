'''6.	Crie uma classe Funcionario que armazena nome e salário, e um método que retorna um aumento salarial de 10%.'''
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
        
    def aumento(self):
        if self.salario < 1300:
            return self.salario * 0.10 + self.salario
        else:
            print("Você nao teve aumento")
            
            
func = Funcionario("Gabriel", 1200)
novo_salario = func.aumento()
print(f"Novo salário: {novo_salario}")