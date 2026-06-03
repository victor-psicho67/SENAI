vb = float(input("Qual é o valor atual de sua bolsa?\n"))
if vb < 1000.0:
    print("Acrecentando aumento de 15%:\n", (vb*0.015)+vb)
else:
    print("Acrecentando aumento de 10%:\n", (vb*0.010)+vb)
