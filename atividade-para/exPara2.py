cont = 0 #inicializando a variavel para contar as idades
for valor in range(1,6):
    idade = int(input("informe sua idade: "))

    if idade >= 18:
            cont = cont + 1
print(f"o total de pessoas maior de 18 é {cont}")