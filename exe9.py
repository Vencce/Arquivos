texto = open("texto.txt", "r")
contador = 0
for linha in texto.readlines():
    letras = linha.replace(" ", "")
    contador += len(letras)
print(contador)
texto.close()
