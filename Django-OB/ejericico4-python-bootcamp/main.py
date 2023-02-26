from vehiculo import Vehiculo



v1 = Vehiculo()

f = open("vehiculo.txt", "w")

f.write(v1.__str__())

f.close()


f = open("vehiculo.txt", "r")

print(f"Vehiculo 1: {f.read()}")

f.close()
