import pymysql

conexao = pymysql.connect(
    host= "localhost",
    user= "root",
    password= "",
    database= "departamento_db"
)

codigo = int(input("qual o código do funcionário deseja apagar? "))

comando = "delete from funcionario where cod_funcionario = %s"

consulta = conexao.cursor()

consulta.execute(comando, codigo)
conexao.commit()

print(consulta.rowcount, "linha(s) foi excluida com sucesso!\n")
conexao.close()