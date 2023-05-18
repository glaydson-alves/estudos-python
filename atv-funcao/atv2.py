while True:
    numA = int(input("informe o valor de A: "))
    numB = int(input("informe o valor de B: "))
    if numA < numB:
        break
def somaImpar(a,b):
    for contador in range(a,b +1):
        if contador % 2 == 1:
            contador = contador + 1
            print(contador)
somaImpar()