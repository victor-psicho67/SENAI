ip = int(input("por favor, me fale o primeiro octeto de seu ip:\n"))
if ip in range(1, 127):
    print("Classe A")
elif ip in range(128, 192):
    print("Classe B")
elif ip in range(192, 223):
    print("Classe C")
