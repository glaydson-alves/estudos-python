class Funcionario:
    def __init__(self, cargo, nome):
        self._cargo = cargo # atributo estão com apenas 1 underline, protegidos
        self._nome = nome
        
    def informacoes(self):
        print(f"Olá {self._nome} seu cargo atual é {self._cargo}\n")
class Gerente(Funcionario):
    def __init__(self, cargo, nome,salario):
        super().__init__(cargo, nome,) # SUPER() SIGNIFICA QUE ESTAMOS USANDO A SEPERCLASSE
        self._salario = salario
    def exibirSalario(self):
        print(f"seu nome é {self._nome} e você ganha {self._salario}\n")