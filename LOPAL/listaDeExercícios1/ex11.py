print("Por favor, me fale suas 3 notas que obteve(de 0 a 10)")
n1 = int(input())
n2 = int(input())
n3 = int(input())
media = int(n1 + n2 + n3)/3
if media >= 7:
    print("Sua media foi:", media, "Aprovado")
elif media >= 5 and media < 7:
    print("Sua media foi: ", media, "Recuperação")
else:
    print("Sua media foi: ", media, "Reprova")
