# while funcionando como loop contado
contador = 1
while contador <=5: #enquanto contador for menor ou igual a 5
    print(contador)
    contador = contador + 1

# while funcionando como loop condicional
'''
senha = ""
while senha != "alves":
    senha = input("informe sua senha: ")
    if senha != "alves":
        print("senha invalida!")
print("senha correta! bem vindo a area 51\n")
'''
# while como se fosse o faça - enquanto
while True: 
    senha = input("informe sua senha: ")
    if senha == "alves":
        break