'''Faça uma classe Produto com atributos nome, preço e quantidade em estoque,
e um método para descontar um valor do estoque.'''

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        
    def desconto(self):
        quantidade_retirada = 1000
        if self.quantidade >= quantidade_retirada:
            self.quantidade -= quantidade_retirada
            print(f"Retirada feita com sucesso! {quantidade_retirada} feijões")
        else:
            print(f"Impossível, pois não há estoque suficiente - Estoque atual: {self.quantidade}")    
        
        
estoquepadrao = Produto("Feijão", 10, 1250)
estoquepadrao.desconto()
print(f"Estoque restante: {estoquepadrao.quantidade}")