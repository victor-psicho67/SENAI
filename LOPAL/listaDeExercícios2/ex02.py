VMB = float(input("Insira o tamanho do arquivo em MB: "))
Mbps = float(input("Insira a velocidade do link: "))
print("O tempo de Download é: ", (Mbps*8)*(VMB))
