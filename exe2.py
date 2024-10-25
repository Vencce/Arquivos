texto = open("texto.txt", "r")
for linha in texto.readlines():
    print(linha, end="")
texto.close()
