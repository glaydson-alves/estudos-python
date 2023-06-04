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



    def atualizarFilme(self):
         conexao = self.conexao()
         while True:
            print("Digite o número correspondente a opção que deseja atualizar ou Voltar ao Menu principal: ")
            opcao = int(input( "1 - Título | 2 - Gênero | 3 - Duração | 4 - Classificação indicativa | 5 - Voltar\n"))
                
            if opcao == 1:
                titulo = input("Informe o título do filme atualizado: ")
                codigo = int(input("Qual o código do filme? "))
                comando = "update filmes set titulo = %s where codigo = %s"
                valores = (titulo, codigo)
                consulta = conexao.cursor()
                consulta.execute(comando, valores)
                conexao.commit()
                print(consulta.rowcount, "Título atualizado com sucesso!\n")
                conexao.close()

            elif opcao == 2:
                genero = input("Informe o gênero do filme atualizado: ")
                codigo = int(input("Qual o código do filme? "))
                comando = "update filmes set genero = %s where codigo = %s"
                valores = (genero, codigo)
                consulta = conexao.cursor()
                consulta.execute(comando, valores)
                conexao.commit()
                print(consulta.rowcount, "Gênero atualizado com sucesso!\n")
                conexao.close()

            elif opcao == 3:
                duracao = int(input("Informe a duração do filme atualizado: "))
                codigo = int(input("Qual o código do filme? "))
                comando = "update filmes set duracao = %s where codigo = %s"
                valores = (duracao, codigo)
                consulta = conexao.cursor()
                consulta.execute(comando, valores)
                conexao.commit()
                print(consulta.rowcount, "Título atualizado com sucesso!\n")
                conexao.close()

            elif opcao == 4:
                classificacao = int(input("Informe a classificação indicativa do filme atualizado: "))
                codigo = int(input("Qual o código do filme? "))
                comando = "update filmes set classificacao_indicativa = %s where codigo = %s"
                valores = (classificacao, codigo)
                consulta = conexao.cursor()
                consulta.execute(comando, valores)
                conexao.commit()
                print(consulta.rowcount, "Título atualizado com sucesso!\n")
                conexao.close()          
            else:
                
                break