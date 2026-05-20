pro1 = int(input("Insira o valor do produto: "))
pro2 = int(input("Insira o valor do produto: "))
pro3 = int(input("Insira o valor do produto: "))
pro4 = int(input("Insira o valor do produto: "))
pro5 = int(input("Insira o valor do produto: "))
subt = pro1 + pro2 + pro3 + pro4 + pro5
print("Sua compra sem imposto: ", subt)
impos = subt * 0.10
print("O valor final de sua compra de 5 produtos com acrecimos de 10% de imposto foi: ", subt + impos)
