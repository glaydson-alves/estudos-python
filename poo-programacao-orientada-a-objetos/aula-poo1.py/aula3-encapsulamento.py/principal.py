from conta import Conta
minhaConta = Conta(123, "chopolin", 4500, 3400)

#minhaConta.relatorio()
minhaConta.saldo = 80500
minhaConta.exibirSaldo()

print("seu limite é", minhaConta.getLimite())
minhaConta.setLimite(90)

# #encapsulamento (proteger parte de dados)
#         modificadores de acesso -> (publicos, privados, protegidos)