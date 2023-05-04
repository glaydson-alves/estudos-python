numero = int(input(" digite um numero entre 1 e 9: "))
if numero < 0 or numero > 9:
    print("digite um número entre 1 e 9: ")
elif numero % 2 == 0:
    for contador in range (1, 11):
        multi = contador * numero
        print(f"{contador} X {numero} = {multi}")
        contador = contador + 1
elif numero % 2 == 1:
    for contador in range(1, 11):
        soma = contador + numero
        print(f"{contador} + {numero} = {soma}")
        contador = contador + 1
        
