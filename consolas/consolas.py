
import datetime

class Console:
    id = 0 # integer
    model = None # ConsoleModel
    fab_date = None # date
    
    def __init__(self, id, model, fab_date):
        self.id = id
        self.model = model
        self.fab_date = fab_date
        
    def __str__(self):
        return "Console( id=" + str(self.id) + ", model=" + self.model.name + ", fab_date=" + str(self.fab_date) + ") "
    
    def __eq__(self, other):
        return(isinstance(other, Console) and other.id==self.id)
    
class ConsoleModel:
    name = ""
    company = None
    puntuacion = 100
    def __init__(self, name, company):
        self.name = name
        self.company = company
        self.puntuacion = 5
        
    def __str__(self):
        return "ConsoleModel(name=" + self.name + ")"
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        return (isinstance(other, ConsoleModel) and other.name==self.name)

class Company:
    name: ""
    
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "Company(name="+self.name+") "
    def __eq__(self, other):
        return( isinstance(other, Company) and other.name==self.name)
        
def console_model(name):
    mls = console_models()
    res = list(filter(lambda x: x.name==name, mls))
    return res[0]
    
def console_models():
    ml = []
    ml.append(ConsoleModel("switch", company_byname("nintendo")))
    ml.append(ConsoleModel("ps4", company_byname("sony")))
    ml.append(ConsoleModel("xboxone", company_byname("microsoft")))
    ml.append(ConsoleModel("3ds", company_byname("nintendo")))
    ml.append(ConsoleModel("psvita", company_byname("sony")))
    return ml

def companies():
    ls = []
    ls.append(Company("nintendo"))
    ls.append(Company("sony"))
    ls.append(Company("microsoft"))
    return ls

def company_byname(name):
    ls = companies()
    generator = (comp for comp in ls if comp.name==name)
    result = list(generator)
    return result[0]
    
def consolesByCompany(consoles, name):
    nintendo = company_byname(name)
    gen = (x for x in consoles if x.company==nintendo)
    resList = list(gen)
    return resList
    


