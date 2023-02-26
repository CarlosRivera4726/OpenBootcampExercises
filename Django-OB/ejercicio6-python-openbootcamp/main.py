'''
En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con 
filter y realizará una suma de todos estos elementos obtenidos mediante reduce.
'''
import functools

#* Lista de numeros
numeros = input("Ingresa numeros separados por coma: ").split(',')

#convertimos de str a int
numeros = [int(x) for x in numeros]

#Obtenemos los numeros impares
numerosImpares = list(filter(lambda x: x % 2 != 0, numeros))
print(f"Numeros Impares: {numerosImpares}")

#Creamos una funcion lambda para que sume los elementos con functools.reduce
sumar = lambda value, element: value+element

#Obtenemos el total
sumaTotal = functools.reduce(sumar, numerosImpares)

print(sumaTotal)
