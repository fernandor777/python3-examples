
import json

def save_json(file_route):
    ''' carga lista de productos de un csv ( | separator) '''
    ls = mock_prods()
    with open(file_route, "w") as jsonf:
        json.dump(ls, jsonf, default=lambda x: x.__dict__)
    
class Product:
    def __init__(self, code, title, price, enabled=True):
        self.code = code
        self.title = title
        self.price = price
        self.enabled = enabled
    def __str__(self):
        return "Product(title="+self.title+",price="+str(self.price)
    def __repr__(self):
        return self.__str__()
    def __eq__(self, other):
        if self.code == other.code:
            return True
        return False

def mock_prods():
    pls = []
    pls.append(Product("f1", "Sombrero", 12.50))
    pls.append(Product("c0", "Corbata", 9.99))
    pls.append(Product("d1", "Camisa", 15.80))
    pls.append(Product("a4", "Pantalon", 20.05))
    pls.append(Product("b9", "Cinturon", 6.60))
    return pls



