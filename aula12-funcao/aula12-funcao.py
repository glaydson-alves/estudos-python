#função sem parêmentro
def somar():
    valor1 = int(input("informe um valor: "))
    valor2 = int(input("informe outro valor: "))
    
    
    print(valor1+valor2)
#somar()

#função com parâmetro
num1 = int(input("informe valor 1: "))        
num2 = int(input("informe valor 2: "))

def multiplicar(a, b):
    print(a * b)
multiplicar(num1,num2)