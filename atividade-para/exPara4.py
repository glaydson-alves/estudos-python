inicial = int(input("informe o valor inicial: "))
final = int(input("informe o valor final: "))
soma = 0

for contador in range (inicial, final + 1):
    soma = soma + contador
print(f"a soma de {inicial} + {final} é {soma}\n")