
altura = float(input("digite sua altura: "))
genero = int(input("digite seu genero, 1 para Masculino ou 2 para Femenino: "))

if genero == 1:
    print((72.7*altura)-58)
elif genero == 2:
    print((62.1*altura)-44.7)
else:
    print("Erro!")