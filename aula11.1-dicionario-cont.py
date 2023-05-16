#inserindo dados em um dicionário
#forma 1

import os
estado = {"uf":"maranhão", "sigla": "MA"}

os.system("cls")
print(estado)

estado["população"] = "20.000.000"
print(estado)

#forma 2

estado.update({"capital":"são luís"})
print(estado)


#removendo itens do dicionário
#forma1

estado.pop("uf")
print(estado)

#forma2
del(estado["população"])
print(estado)

#forma3 - apaga todo o conteúdo

estado.clear()
print(estado)