tick = ["Ana", "Carlos", "João", "Ney", "CR7", "Sans"]
print("Lista de chamados: \n", tick, "\n Qual chamado já foi concluido?(apenas um)")
chamadocon = input()
if chamadocon == "Ana":
    print("Lista atual: ", "Carlos,", "João,", "Ney,", "CR7", "e Sans")
elif chamadocon == "Carlos":
    print("Lista atual: ", "Ana,", "João,", "Ney,", "CR7", "e Sans")
elif chamadocon == "João":
    print("Lista atual: ", "Ana,", "Carlos,", "Ney,", "CR7", "e Sans")
elif chamadocon == "Ney":
    print("Lista atual: ", "Ana,", "Carlos,", "João,", "CR7", "e Sans")
elif chamadocon == "CR7":
    print("Lista atual: ", "Ana,", "Carlos,", "João,", "Ney", "e Sans")
else:
    print("Lista atual: ", "Ana,", "Carlos,", "João,", "Ney", "e CR7")
