from regladetres import *

class VelocidadConverter:
    """ Conversor de unidades de velocidad: km/h mi/h """
    unidad_salida = "mi/h"
    unidades_posibles = ("mi/h","km/h") # tuple de unidades posibles
    
    def convert(self, valor, unidad):
        mult = 1.61
        if unidad==self.unidad_salida:
            return valor
        self.validate_units(unidad)
        if unidad == "km/h":
            mult = 1/mult
        return valor * mult
    
    def validate_units(self, unidad_salida):
        return True