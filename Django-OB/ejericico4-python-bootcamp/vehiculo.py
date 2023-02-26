

class Vehiculo(object):
    def __init__(self):
        self.ruedas = 4
        self.puertas = 4
        self.ventanas = 4
        self.cilindraje = 200
        self.km = 400
    

    def getRuedas(self):
        return self.ruedas

    def getPuertas(self):
        return self.puertas

    def getVentanas(self):
        return self.ventanas

    def getCilindraje(self):
        return self.cilindraje
        
    def getKm(self):
        return self.km

    def __str__(self):
        return f"Este vehiculo tiene: \n{self.ruedas} ruedas\n{self.puertas} puertas\n{self.ventanas} ventanas\n{self.cilindraje} CC\n{self.km} KM/h"
    
