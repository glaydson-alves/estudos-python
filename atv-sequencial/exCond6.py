CarroTipo1 = 8
CarroTipo2 = 9
CarroTipo3 = 12

Carro = int(input("escreva qual o tipo do seu carro, 1, 2 ou 3: "))
percurso = float(input("informe quantos kilometros é seu percurso e eu mostro quantos litros de combustivél será necessario: "))

if Carro == CarroTipo1:
    litro = percurso / CarroTipo1
    print("será necessário", litro, "litros para seu percurso" )
elif Carro == CarroTipo2:
    litro = percurso / CarroTipo2
    print("será necessário", litro, "litros para seu percurso")
else:
    litro = percurso / CarroTipo3
    print("será necessário", litro, "litros para percurso") 