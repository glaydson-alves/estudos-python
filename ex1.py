vetImpar = []
vetPar = []
quantI = 0
quantP = 0
somaI = 0
somaP = 0

for contador in range (1, 11):
    if contador % 2 == 0:
        vetPar.append(contador)
        quantP = quantP + 1
        somaP = somaP + contador
    if contador % 2 == 1:
        vetImpar.append(contador)
        quantI = quantI + 1
        somaI = somaI + contador
        
print(f"esses são os números pares{vetPar}, foram {quantP} no total, e a soma entre ele é {somaP}")
print(f"esses são os númeroa impares{ vetImpar}, foram {quantI} no total, e a soma entre eles é {somaI}")
