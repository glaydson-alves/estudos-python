from funcionario import Funcionario

f1 = Funcionario("alves", "programador")

print(f"seu nome é {f1.getNome()}")

f1.setNome("isabela")

print(f"seu nome é {f1.getNome()}")


print(f"seu cargo é {f1.cargo}")
f1.cargo = "gerente"
print(f"seu cargo é {f1.cargo}")