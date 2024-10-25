texto = open("texto.txt", "r")
contador = 0
for linha in texto.readlines():
    palavras = linha.split()
    contador += len(palavras)
print(contador)
texto.close()
