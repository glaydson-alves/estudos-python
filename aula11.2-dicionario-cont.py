#{} cria dicionário(dict), enquanto [] cria lista(list).
import os
pessoa = dict()
grupo = list()

grupo.append({"nome":"alves", "idade":23})
grupo.append({"nome":"beto", "idade":28})
grupo.append({"nome":"carlos", "idade":45})
os.system("cls")
'''
for contador in range(0, 3):  # esse for serve para receber as informações de PESSOA, depois através do grupo.append é jogado essas informações para GRUPO
    pessoa["nome"] = input("qual o seu nome: ")
    pessoa["idade"] = int(input("qual a sua idade: "))
    os.system("cls")
    
    grupo.append(pessoa.copy()) #criando copias do dicionário para a lista (copiando e limpando)

print(grupo)
'''
#acessando itens do dicionário

print (grupo,"\n")
for contador in range (0,3): #esse for está mostrando apenas o conteudo da linha
    print(f"{grupo[contador]['nome']}: {grupo[contador]['idade']}")
    
#outra forma de acessar itens do dicionário
    
for linha in grupo:
    for chave, valor in linha.items():
        print(f"{chave} -- {valor}")