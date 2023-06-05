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
        print("Digite o número correspondente a opção que deseja atualizar ou Voltar ao Menu principal: ")
        opcao = int(input( "1 - Título | 2 - Gênero | 3 - Duração | 4 - Classificação indicativa | 5 - Voltar\n"))      
        if opcao == 1:
            campo = "titulo"
        elif opcao == 2:
            campo = "gerero"
        elif opcao == 4:
            campo = "classificacao_indicativa"
            valor = input(f"informe o(a) {campo} do Filme atualizado: ")
            codigo = int(input("informe o código do Filme que deseja atualizar: "))
            f1.atualizarFilme(campo, valor, codigo)
    elif menu == 4:
        f1.deletarFilme()
    elif menu == 5:
        break
os.system("cls")
    















