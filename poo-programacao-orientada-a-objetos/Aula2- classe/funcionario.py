class Funcionario:
    # Criando o método construtor 
    def __init__(self, nome, cargo, salario): #classe com "__" são class especiais \ __init__ é usado para iniciar a class sem valores
        # criando os atributos da classe utilizando método 
        # construtor. Nesse caso precisamos passar os parâmentros que 
        # serão usados como valores dos atributos da classe. 
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        
    
    
    def exibir_dados(self): #sempre se usa selfe na def da class
        print(f"Olá {self.nome} seu cargo é {self.cargo} seu salário é {self.salario}")# usa-se o self para informar que as variáveis pertencem a class que a função se encontra
        
  