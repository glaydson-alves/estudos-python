#funcao com retorno

nome = input("informe seu nome: ")

def contse(texto):
    #print (f" O nome possui o total de {len(texto)} caracteres")
    return len(texto)
print(contse(nome))