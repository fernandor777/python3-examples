import datetime

class LifeBeing:
    ''' LifeBeing '''
    def __init__(age):
        self.age = age
    

class Human(LifeBeing):
    def __init__(name, age):
        super().__init__(age)
        self.name = name
        self.birthyear = calculate_birth_year(age)
    def calculate_birth_year(age):
        now = datetime.datetime.now()
        curryear = now.year
        byear = curryear - age
        return byear
        
def makehuman(name, age):
    return Human(name, age)
    
        
class Age100App:
    def __init__():
        self.iname = None
        self.iage = None
        self.human = None
    def run():
        self.iname = input("Enter name:")
        self.iage = input("Enter age:")
        human = makehuman(self.iname, self.iage)
        print("You will have 100 years in : ", human.birthyear+100)
        
def makeapp():
    return Age100App()
        