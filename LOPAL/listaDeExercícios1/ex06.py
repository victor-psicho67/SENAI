print("de 0 a 10 qual é sua nota?")
nota = int(input())
if nota >= 7:
    print("Aprovado")
elif nota >= 5 and nota < 7:
    print("Recuperação")
else:
    print("Reprovado")
