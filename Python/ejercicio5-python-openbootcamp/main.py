'''
Crea un script que le pida al usuario una lista de países (separados por comas). Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). Finalmente,
muestra por consola la lista de países ordenados alfabéticamente y separados por comas.
'''
#* Creamos la variable paises y con split la volvemos una lista
paises = input("Ingresa una lista de paises separados por coma ex:(Colombia, Argentina, etc): ").split(", ")

#* Hacemos el tratamiento de convertir la lista en un set  y convertimos nuevamente en list para que quede en lista y hacemos el sort
paises = sorted(set(paises))

strPaises = ","

print(strPaises.join(paises))


