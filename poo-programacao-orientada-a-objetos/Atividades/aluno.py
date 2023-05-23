class Aluno:
    def __init__(self, nome, matricula, telefone):
        self.nome= nome
        self.matricula = matricula
        self.telefone = telefone
    def exibir_dados(self):
        print(f"Olá {self.nome} sua matrícula é {self.matricula} e seu contato é{self.telefone}")