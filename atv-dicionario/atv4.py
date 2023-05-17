import os
playlist = []
musica = {}
for contador in range (2):
    nome = input("informe o nome da música: ")
    artista = input("qual o nome do artista: ")
    tempo = float(input("qual a duração da música: "))
    
    musica[nome] = {"artista":artista, "duracao": tempo}
    os.system("cls")
    
    playlist.append(musica.copy())
    musica.clear()
    
    print(playlist)


