class Pessoa:
    # Atributos (serão sempre variáveis)
    nome= "fulano"
    idade= 30
    altura= 1.65
    
    # métodos sempre serão def
    def falar(self, texto): # self é um parâmetro obrigatório do python que informa que o método pértence a própria classe que foi criada
        print(texto)
        
        
        
        
        
#Instanciar é criar um obejto (usando variável) a partir de uma class
    
pessoa1= Pessoa() #nete caso, pessoa1 recebe a class, e pessoa1 passa a ser um objeto com os atributos da classe
pessoa1.nome = "José" # A alteração será feito no objeto (pessoa1), não alterando a estrutura da classe
print(pessoa1.nome, pessoa1.idade)

pessoa1.falar("Olá mundo")

