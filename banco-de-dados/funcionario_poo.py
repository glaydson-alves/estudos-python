import pymysql
class Funcionario:
    def conexao(self):
        conect = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="departamento_db"
        )
        return conect
  
  
    def inserir(self, codigo, nome, salario, cargo):
        conexao = self.conexao() # estamos chamando o método que irá conectar ao banco
        
        comando = "insert into funcionario values(%s,%s,%s,%s)"
        
        valores = (codigo, nome, salario, cargo)
        consulta = conexao.cursor()
        consulta.execute(comando, valores)
        conexao.commit()
        print(consulta.rowcount, "linha inserida com sucesso!\n")
        conexao.close()
  
        
    def consultar(self):
        conexao = self.conexao()
        comando = "select * from funcionario"
        consulta = conexao.cursor()
        consulta.execute(comando)
        resultado = consulta.fetchall()
        print(resultado, "\n")
        conexao.close()

        for itens in resultado:
            print(f"nome: {itens[1]}, cargo : {itens[3]}")
        print("\n")
        
    