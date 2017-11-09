
class CarHangar:
    cars = []
    def __init__(self, car_list):
        self.cars = car_list
        self.cars.sort(key=lambda x: x.anio, reverse=True)
    def cars_order_marca(self):
        cars2 = sorted(self.cars, key=lambda x: x.marca, reverse=False)
        return cars2
    
def generate_car_list():
    cars = []
    cars.append(Car("chevrolet","sail",2013))
    cars.append(Car("audi","m3",1998))
    cars.append(Car("hyundai","",2003))
    cars.append(Car("kia","rio",2010))
    cars.append(Car("kia","sportage",2017))
    return cars
    
class Car:
    anio = 0
    marca = ""
    modelo = ""
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
    def __str__(self):
        return "Car() marca: " + self.marca + ", modelo: " + self.modelo + ", año: " + str(self.anio)
    def __repr__(self):
        return "Car() marca: " + self.marca + ", modelo: " + self.modelo + ", año: " + str(self.anio)
        
        