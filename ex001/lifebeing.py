import datetime

class LifeBeing:
    ''' LifeBeing '''
    def __init__(self, age):
        self.age = age
    

class Human(LifeBeing):
    def __init__(self, name, age):
        super().__init__(age)
        self.name = name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        self.age = value
        self.birthyear = self.calculate_birth_year(value)
    def calculate_birth_year(self, age):
        now = datetime.datetime.now()
        curryear = now.year
        byear = curryear - age
        return byear
    
    
        
def makehuman(name, age):
    return Human(name, age)
    
        
class Age100App:
    def __init__(self):
        self.iname = None
        self.iage = None
        self.human = None
    def run(self):
        self.iname = input("Enter name:")
        self.iage = int(input("Enter age:"))
        human = makehuman(self.iname, self.iage)
        print("You will have 100 years in : ", human.birthyear+100)
        
def makeapp():
    return Age100App()
        