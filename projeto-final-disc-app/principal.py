from arquivo import Filme
import os

f1 = Filme()

while True:
    print("MENU DB CINEMA")
    print("Escolha uma Opção Abaixo:")
    menu = int(input("1 = Cadastrar | 2 = Consultar | 3 = Atualizar | 4 = Deletar | 5 = Sair\n"))

    if menu == 1:
        cod = int(input("Informe o código do Filme: "))
        titulo = input("Digite o nome do Filme: ")
        genero = input("Informe o gênero do Filme: ")
        duracao = int(input("Qual a duração do Filme: "))
        classificacao = int(input("Informe a classiicação indicativa: "))
        f1.cadastrarFilme(
            codigo= cod,
            titulo= titulo,
            genero= genero,
            duracao= duracao,
            classificacao_indicativa= classificacao
        )
    elif menu == 2:
        f1.consultarFilme()
    elif menu == 3:
        f1.atualizarFilme()
    elif menu == 4:
        f1.deletarFilme()
    elif menu == 5:
        break
os.system("cls")
    

















# # codigo = int(input("Digite o código do Filme: "))
# # titulo = input("Digite o título do Filme: ")
# # genero = input("Digite o gênero do Filme: " )
# # duracao = int(input("Digite a duração do Filme: "))
# # classificacao_indicativa = int(input("Digite a classificação indicativa do Filme: "))

# # cadastro = (codigo, titulo, genero, duracao,classificacao_indicativa)
# #f1.cadastrarFilme(1,"Star Wars", "Fantasia científica",136,12)

# f1.consultarFilme()