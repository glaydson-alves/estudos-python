import os
lista = []
pessoas = {}
for contador in range (0,7):
    nome = input("informe o seu nome: ")
    pessoas[nome] = int(input(F"Olá {nome}, informe seu número de telefone: "))
    os.system("cls")
    
    lista.append(pessoas.copy()) #copiar o conteúdo do dicionário para a lista
    pessoas.clear() #limpa o conteudo do dicionário
print(lista)


