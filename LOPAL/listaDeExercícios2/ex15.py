frase = input("Digite uma frase\n")
for contador in frase:
     a = frase.count("a")
     e = frase.count("e")
     i = frase.count("i")
     o = frase.count("o")
     u = frase.count("u")
     contadorFinal = a + e + i + o + u
print("Numero de vogais:", contadorFinal)
