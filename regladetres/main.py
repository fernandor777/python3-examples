#!/usr/bin/python
import sys
from regladetres import *

print("Si A nos da B, entonces X nos daria: ")

a = input("A=")
b = input("B=")
x = input("X=")

rd3 = ReglaDeTres(a,b,x)

print("Resultado = " + str(rd3.calcular()))


