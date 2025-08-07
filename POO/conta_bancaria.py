class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.__titular = titular
        self.__saldo = saldo_inicial
        
    def depositar(self, valor):
        if valor >0:
            self.__saldo += valor 
            print(f"Depósito de R${valor} realizada com sucesso")
        else:
            print("Valor de depósito inválido")
            
    def sacar(self, valor):
            if 0 < valor <= self.__saldo:
                self.__saldo -= valor 
                print(f"Saque de R${valor} realizado com sucesso")
            else:
                print("Saldo Insuficiente ou valor inválido para saque")
                
                
    def consultar_saldo(self):
        return self.__saldo 

'''Getter | Setter:
Getter: é um método usado para obter(LER) o valor de um atributo privado de uma classe|

Setter: É usado para definir(escrever) ou alterar o valor de um atributo privado de uma classe'''

#Getter para o títular(somente leitura)

@property
def titular(self):
    return self.__titular

#Usar a classe
conta = ContaBancaria("João Silva", 1000)
print(conta.titular) #Saida: João Silva
print(conta.consultar_saldo()) #Saida: 1000


