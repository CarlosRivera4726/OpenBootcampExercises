numeroInicial = int(input("Ingrese el numero inicial: "))
numeroFinal = int(input("Ingrese el numero final: "))
aux = 0

for numeroImpar in range(numeroInicial, numeroFinal):
    if numeroImpar % 2 != 0:
        print(numeroImpar, end=", ")
    if aux == 10:
        print()
        aux = 0
    aux += 1
print()
