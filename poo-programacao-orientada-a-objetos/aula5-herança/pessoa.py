class Pessoa: # superclasse ou classe mãe
    def __init__(self, nome, idade):
        self._nome = nome # ao utilizar apenas 1 underline, dizemos que o atributo está com o modificador protegido, ou seja, as classes filhas tem acesso aos atributos da classes mãe.
        self._idade = idade
    
    def relatorio (self):
        print("sou uma pessoa.")
        print(f"Olá {self._nome}, sua idade é {self._idade}\n")
        
class Aluno(Pessoa):
    def mostraAluno(self):
        print(f"sou aluno e meu nome é {self._nome}\n")
        
class Professor(Pessoa):
    def mostraProfessoar(self):
        print(f"sou professor e meu nome é {self._nome}\n")