texto = open("texto.txt", "r")
saida = open("modificado.txt", "w")
for linha in texto.readlines():
    saida.write(linha.replace("mundo", "Python"))
texto.close()
saida.close()
