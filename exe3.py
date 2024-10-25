texto = open("texto.txt", "r")
contador = 0
for linha in texto.readlines():
    contador += 1
print(contador)
texto.close()
