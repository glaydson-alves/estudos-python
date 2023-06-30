salario = float(input("digite seu salário: "))
financiamento = float(input("digite o valor do seu financiamento: "))

if financiamento <= (5*salario):
    print("** Financiamento Concedido **")
    print("Obrigado por nos consultar!")
else:
    print("** Financiamento Negado **")
    print("Obrigado por nos consultar!")
