from list_order import *

print("carros sin ordenar:")
print(generate_car_list())

hangar = HangarOmega(generate_car_list())
hangar.pilotos = gen_pilotos_list()

print("diferencia con y2k")
print(hangar.maplist_y2kdiff())
print("promedio de anios:")
print(hangar.year_promd())
print("filtro marca kia:")
print(hangar.filter_cars("kia"))


# print("---")
# print("carros ordenados por año por default:")
# print(hangar.cars)

# print("---")
# print("Ahora orden por marca y luego modelo:")
# cars_ord = sorted(hangar.cars_order_marca(), key=lambda x: x.modelo, reverse=False)
# print(cars_ord)

# print("---")
# print("Pilotos por orden alfabetico:")
# print(hangar.pilotos_order())

