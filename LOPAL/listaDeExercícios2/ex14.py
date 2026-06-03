totalItens = []
resp = ""
while resp != "sair":
    its = input("Digite o nome de cada item do supermercado:\n ")
    totalItens.append(its)
    resp = input("Gostaria de continuar adicionando itens?(sim/sair)")
print(totalItens)
