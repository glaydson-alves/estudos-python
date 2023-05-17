import os
lista = []
pratos = {}
for contador in range (0,2):
    nome = input("informe o nome do prato: ")
    pratos[nome] = float(input(f"informe o valor desse prato: "))
    os.system("cls")
    
    lista.append(pratos.copy()) #copiar o conteúdo do dicionário para a lista
    pratos.clear() #limpa o conteudo do dicionário
print(lista)


