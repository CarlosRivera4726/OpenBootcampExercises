from operacionesBasicas import Operaciones


if __name__ == '__main__':
    #Create object of type Operaciones
    operacion = Operaciones()

    #using functions
    print(f"La suma es: {operacion.sumar(5, 6)}")
    print(f"La resta es: {operacion.restar(5, 6)}")
    print(f"La multiplicacion es: {operacion.multiplicar(5, 6)}")
    print(f"La division es: {operacion.dividir(5, 6)}")
