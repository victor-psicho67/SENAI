lv = float(input("qual é o valor do livro?\n"))
if lv > 80.00:
    print("Você adiquiriu um desconto de 10% sobre o valor do livro, o valor final é: ", (lv*0.010)+(lv))
else:
    print("Pagamento ocorrendo normalmente, valor do produto continua ", lv)
