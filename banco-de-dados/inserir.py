# CRUD
# C = CREAT
# R = READ
# U = UPDATE
# D = DELETE

import pymysql
#ESTABELECENDO A CONEXÃO
conexao = pymysql.connect(
    host= "localhost",
    user= "root",
    password= "",
    database= "departamento_db"
)

#nserindo dados no banco 

codigo = int(input("informe o código do funcionário: "))
nome = input("informe o nome do funcionário: ")
salario = float(input("informe o salário do funcionário: "))
cargo = input("informe o cargo do funcionário: ")

#colocamos %s no lugar dos dados, para evitar possíveis ataques de sql injecton. Isso é uma implementação da biblioteca pymysql
comando = "insert into funcionario values(%s, %s, %s, %s)"

campos = (codigo, nome, salario, cargo) # criando uma tuple com os dados que serão substituidos no comando

consulta = conexao.cursor() #cursor() é o objeto que irá interagir diretamente com o banco de dados

consulta.execute(comando,campos)

conexao.commit() #grava os dados no banco

print(consulta.rowcount, "linha(s) inserida(s) com sucesso\n") #rowcount  faz a contagem de linhas
conexao.close() # encerrar conexão