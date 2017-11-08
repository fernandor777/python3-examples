#!/usr/bin/python
from velocidad_convert import *

velocidad = input("velocidad? ")
velocidad = float(velocidad)
unidad = input("Unidad? (km/h, mi/h) ")
unidad_salida = input("Unidad a convertir? (km/h, mi/h)")

vconverter = VelocidadConverter()
vconverter.unidad_salida = unidad_salida
print("Resultado: " + str(vconverter.convert(velocidad, unidad)) + unidad_salida)





