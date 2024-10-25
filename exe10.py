texto = open("numeros.txt", "r")
soma = 0
for linha in texto.readlines():
    soma += int(linha.strip())
print(soma)
texto.close()
