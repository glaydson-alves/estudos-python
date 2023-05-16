lista = ["joão", 30, "cohab"]
pessoa = {
    "nome":"maria",
    "idade": 24,
    "bairro": "renascença"
}

print (lista[0])
print(pessoa,"\n")

#exibindo as chaves utilizando o comando keys()
print(pessoa.keys())

#exibindo os valores utilizando o comando values()
print(pessoa.values())

#exibindo tamto a chave como valor utilizando o comando items()
print(pessoa.items())

#exibindo o dicionário mais detalhado

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")