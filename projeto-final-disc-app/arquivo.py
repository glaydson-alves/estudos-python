import pymysql

class Filme:
    def conexao(self):
        conect = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="cinema_db"
        )
        return conect
    
    def cadastrarFilme(self, codigo, titulo, genero, duracao, classificacao_indicativa):
        conexao = self.conexao()
        comando = "insert into filmes values (%s,%s,%s,%s,%s)"
        cadastros = (codigo, titulo, genero, duracao, classificacao_indicativa)
        consulta = conexao.cursor()
        consulta.execute(comando, cadastros)
        conexao.commit()
        print(consulta.rowcount, "cadastro realizado com sucesso!\n")
        conexao.close()



    def consultarFilme(self):
        conexao = self.conexao()
        comando = "select * from filmes"
        consulta = conexao.cursor()
        consulta.execute(comando)
        resultado = consulta.fetchall()
        print(resultado, "\n")
        conexao.close()

        for itens in resultado:
            print(f"código: {itens[0]} | título: {itens[1]} | gênero: {itens[2]} | duração: {itens[3]} min | classificaçao indicativa: {itens[4]}")
        print("\n")



    def deletarFilme(self):
        conexao = self.conexao()
        codigo = int(input("Qual o código do Filme que deseja apagar? "))
        comando = "delete from filmes where codigo = %s"
        consulta = conexao.cursor()
        consulta.execute(comando, codigo)
        conexao.commit()
        print(consulta.rowcount, "Filme foi deletado com sucesso!\n")
        conexao.close()



    def atualizarFilme(self, campo, valor,codigo,):
        conexao = self.conexao()
        comando = f"update filmes set {campo} = %s where codigo = %s"
        valores = (valor, codigo)
        consulta = conexao.cursor()
        consulta.execute(comando, valores)
        conexao.commit()
        print(consulta.rowcount, "atualizado com sucesso!\n")
        conexao.close()
    
