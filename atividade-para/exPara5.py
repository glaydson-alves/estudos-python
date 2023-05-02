valor = int(input("insira uma valor qualquer: "))

maior = 0 
posicao = 0

for contador in range (1, valor+1):
    item = int(input("informe um valor: "))
    if item >= maior:
        maior = item
        posicao = contador
print(f"o maior valor é {maior} e está na posição {posicao}\n")