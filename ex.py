for ascendente in range (1, 11):
    print(ascendente, end=" ")
for descendente in range (10, 0, -1):
    print(descendente, end=" ")

# correção ============================================

contador = 1
valor = 10

while contador <= 10:
        print(f"{contador} - {valor}")
        contador = contador + 1 # contador  +=1
        valor -= 1 # é o mesmo que valor = valor - 1