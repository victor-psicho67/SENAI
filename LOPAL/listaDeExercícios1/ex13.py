print("insira uma senha que contenha 8 ou mais caracteres")
senha = input()
while len(senha) < 8:
    print("Senha invalida")
    senha = input("insira uma senha com 8 ou mais digitos: ")
print("Senha valida")
