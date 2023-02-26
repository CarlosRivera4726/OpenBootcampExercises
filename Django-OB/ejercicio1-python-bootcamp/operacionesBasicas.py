

class Operaciones(object):
    
    def __init__(self):
        pass
    
    def sumar(self, a=0, b=0):
        return a + b

    def restar(self, a=0, b=0):
        return a - b

    def multiplicar(self, a=0, b=0):
        return a * b

    def dividir(self, a=0, b=0):
        try:
            return a / b
        except:
            return "Error"
