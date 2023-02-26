# Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros
# h -> altura, b -> base

areaTriangulo = lambda h, b: (b*h) / 2


# otra función que calcule el área de un círculo recibiendo el radio del mismo.
# r -> radio
# PI = 3.141592
PI = 3.141592
areaCirculo = lambda r: PI * ( r**2 )


# llamamos a las funciones
# Area del triangulo
print( "Area Triangulo: \n" )
print(areaTriangulo(float(input("Ingresa la altura: ")), float(input("Ingresa la base: "))))

# Area del circulo

print("Area del Círculo: \n")
print(areaCirculo(float(input("Ingresa el radio: "))))


