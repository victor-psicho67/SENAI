print("MENU INTERATIVO")
resp = input("Gostaria de cadastrar um usuario(Sim/não) \n")
while resp == "Sim":
    us = input("Insira seu usuario: ")
    lista = ["Ana", "Carlos", "João", "Ney", "CR7", "Sans", us]
    print("Lista atual: ", lista)
    print("Sair ou Sim?(Caso click Sair seu usuario sera cadastrado, caso Sim você podera cadastrar outro usuario)")
    resp = input("")
