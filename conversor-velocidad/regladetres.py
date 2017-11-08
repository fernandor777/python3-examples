
class ReglaDeTres:
    """ Calcula una regla de tres simple y directa """
    a = 0
    b = 0
    x = 0
    
    def __init__(self, a, b, x):
        self.a = a;
        self.b = b;
        self.x = x;
        
    def calcular(self):
        return (self.x*self.b)/self.a
