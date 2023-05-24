class Conta:
    def __init__(self, numero, titular, saldo, limite=100):
        self.__numero = numero # em python tormaos um elemento privado com 2 underlines. com 1 undeline ele está protegido. com nenhum underline, está publlico
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite #esse atributo possui um valor padrão de forma que o usuário  poderá ou não informar este valor

    def relatorio(self):
        print(f"Olá {self.__titular} o número da sua conta é {self.__numero} e o salda atual é R$ {self.__saldo} e o seu limite é R$ {self.__limite}")
        
    def exibirSaldo(self):
        print(f" seu saldo é R${self.__saldo}")
    
    #o metodo get irá retornar ou exibir i valor do atributo
    def getLimite(self):
        return self.__limite
    #o metodo set irá alterar o conteudo do atributo, sem exibir nada
    def setLimite(self, valor):
        if valor < 0:
            print("Valor menor que zero, informe outro valor")
        else:
            self.__limite = valor
    # #metodos
    # getSaldo
    # setSaldo
    # vamos modificar o atributo saldo com @property e @setter
    @property
    def saldo(self):
        print(f"Olá, seu saldo é {self.__saldo}\n")
        
    @saldo.setter
    def saldo(self, valor):
        if valor <= 0:
            print("você não pode inserir valor negativo ou zero\n")
        else:
            self.__saldo = valor