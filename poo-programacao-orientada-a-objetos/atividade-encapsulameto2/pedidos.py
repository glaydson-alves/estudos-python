class Servico:
    def __init__(self,):
        self.pedido = 0
    
    def novoPedido(self, valor):
        self.pedido = valor
    
    def cancelarPedido(self,valor):
        self.pedido = self.pedido - valor
    
    def exibirPedido(self):
        print(self.pedido)