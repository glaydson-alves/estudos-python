a = float(input("informe o lado A: "))
b = float(input("informe o lado B: "))
c = float(input("informe o lado C: "))

if a < b+c and b < a+c and c < a+b:
    print("temos um triângulo. \n")
else:
    print("você não encontrou um triângulo. \n")