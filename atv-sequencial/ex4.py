
lata = 350
garrafa1 = 600
garrafa2 = 2000

compraL = int(input("informe a quantidade de refri de 350 ml que deseja comprar: "))
compraG1 = int(input("informe a quantidade de refri de 600 ml que deseja comprar: "))
compraG2 = int(input("informe a quantidade de refri de 2 litros que deseja comprar: "))


print("a quantidade total em ml de refri comprado foi", (compraL*lata) + (garrafa1*compraG1) + (garrafa2*compraG2))