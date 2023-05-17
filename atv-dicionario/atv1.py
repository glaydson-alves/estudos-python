import os
lista = []
produtos = {}
for contador in range (0,5):
    nome = input("informe o nome do produto: ")
    produtos[nome] = int(input(F"informe a quantidade de {nome}: "))
    os.system("cls")
    
    lista.append(produtos.copy()) #copiar o conteúdo do dicionário para a lista
    produtos.clear() #limpa o conteudo do dicionário
print(lista)


