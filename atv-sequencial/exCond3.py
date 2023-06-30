salario = float(input("digite seu salário: "))
if salario <= 600 :
    print("Parabéns! você ganhou uma bonificação, seu novo salário é:", (salario*30) / 100 + salario)
else :
    print("ok! seu salário é maior que R$600,00")
    print("volte ao trabalho!")