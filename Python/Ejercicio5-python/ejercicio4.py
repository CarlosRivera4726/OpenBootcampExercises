esBisiesto = lambda y: y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
aux = "Es bisiesto" if esBisiesto(int(input("Ingrese el año: "))) else "No es bisiesto"
print(aux)
