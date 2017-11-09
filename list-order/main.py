from list_order import *

print("carros sin ordenar:")
print(generate_car_list())

hangar = CarHangar(generate_car_list())

print("---")
print("carros ordenados por año por default:")
print(hangar.cars)

print("---")
print("Ahora orden por marca y luego modelo:")
cars_ord = sorted(hangar.cars_order_marca(), key=lambda x: x.modelo, reverse=False)
print(cars_ord)


