import pymysql

conexao = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "departamento_db"
)

comando = "select * from funcionario"

consulta = conexao.cursor()

consulta.execute(comando)
# exibir a consulta do banco

resultado = consulta.fetchall() # fetchall irá trazer todas as linhas de registros dentro do banco

print(resultado, "\n")
conexao.close()

for itens in resultado:
    print(f"nome: {itens[1]}, cargo : {itens[3]}")
print("\n")