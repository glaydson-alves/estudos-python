texto = "técnico em desenvolvimento de sistemas"
print("********* titulo *********")
print("*"*10)
print(texto)

idade = int(input("digite a sua idade, e lhe mostrarei em #, hahahaha: "))

print("sua idade em # é ")
print("#"*idade)

#manipulando textos(string)
print (f"o total de letras é {len (texto)}") # len() vem  de length, que significa total
print(texto,upper())# upper ()coloca todo texto em maiúscilo
print(texto.capitalize())# coloca a 1ª letra em maiúsculo

print(texto,replace("sistemas","web")) #replace troca um texto por outro

#trabalhando com fatiamento
print("fatiando a variavél texto")
print(texto[:3]) # vai exibir todo o texto até a posição 2, no caso a posição 3 não conta.
print(texto[3:]) # vai exibir todo o texto a partir da posição 3
print(texto[3:10]) # vai exibir todo o texto que está na posição 3 até 10
