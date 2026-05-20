np = input("Insira o nome do produto: ")
qa = int(input("Insira a quantidade atual: "))
qv = int(input("Insira a quantidade vendida: "))
if qv - qa >= 0:
    print("Fora de estoque")
else:
    print("Ainda em estoque")
