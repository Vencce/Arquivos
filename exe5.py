texto1 = open("texto.txt", "r")
texto2 = open("copia.txt", "r")
saida = open("combinado.txt", "w")
for linha in texto1.readlines():
    saida.write(linha)
for linha in texto2.readlines():
    saida.write(linha)
texto1.close()
texto2.close()
saida.close()
