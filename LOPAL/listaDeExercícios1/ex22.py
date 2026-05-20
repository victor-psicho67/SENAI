print("Cinema assentos 3 por 3: ")
assentos = [
    ["Assento_1", "Assento_2", "Assento_3"],
    ["Assento_4", "Assento_5", "Assento_6"],
    ["Assento_7", "Assento_8", "Assento_9"]
]
for cinema in assentos:
    print(cinema)
escolha = input("Por favor escolha um dos assentos acima: ")
for l in range(len(assentos)):
    for c in range(len(assentos[l])):
        if assentos[l][c] == escolha:
            assentos[l][c] = "Ocupado"
print("Lista de assentos atualizado:")
for cinema in assentos:
    print(cinema)
