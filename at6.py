import os # importando biblioteca para trabalhar com recursos do sistema operacional
dentroIntervalo = 0
foraIntervalo = 0
contador = 1

os.system("cls") # limpar a tela, usando a biblioteca
while contador <= 5:
    valor = int(input(f"informe o valor {contador}º: "))
    if valor >= 10 and valor <= 20:
        dentroIntervalo += 1
    else:
        foraIntervalo += 1
    contador += 1
print(f"vaalores dentro do intervalo: {dentroIntervalo}")
print(f"vaalores fora do intervalo: {foraIntervalo}")