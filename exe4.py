texto = open("texto.txt", "r")
saida = open("copia.txt", "w")
for linha in texto.readlines():
    saida.write(linha)
texto.close()
saida.close()
