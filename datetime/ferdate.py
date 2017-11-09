import datetime

class DateUtils:
    
    def month_name(self, dt1=datetime.datetime(2009, 3, 5, 18, 00)):
    # dt1 = datetime.datetime(2009, 10, 5, 18, 00) for example
        md1 = self.month_dict() 
        return md1[dt1.month]
    
    def month_dict(self):
        mlist = self.month_ident_list()
        md1 = {}
        for cmonth in mlist:
            md1[cmonth.number] = cmonth.name
        return md1
    
    def month_dict_old(self):
        md1 = {1:"enero", 2:"febrero", 3:"marzo", 4:"abril", 5:"mayo", 6:"junio", 7:"julio"}
        md1[8] = "agosto"
        md1[9] = "septiembre"
        md1[10] = "octubre"
        md1[11] = "noviembre"
        md1[12] = "diciembre"
        return md1
    
    def month_ident_list(self):
        months = []
        months.append(MonthIdentifier(1,"enero"))
        months.append(MonthIdentifier(2,"febrero"))
        months.append(MonthIdentifier(3,"marzo"))
        months.append(MonthIdentifier(4,"abril"))
        months.append(MonthIdentifier(5,"mayo"))
        months.append(MonthIdentifier(6,"junio"))
        months.append(MonthIdentifier(7,"julio"))
        months.append(MonthIdentifier(8,"agosto"))
        months.append(MonthIdentifier(9,"septiembre"))
        months.append(MonthIdentifier(10,"octubre"))
        months.append(MonthIdentifier(11,"noviembre"))
        months.append(MonthIdentifier(12,"diciembre"))
        return months

class MonthIdentifier:
    name = "enero"
    number = 1
    
    def __init__(self, number, name):
        self.name = name
        self.number = number
    
        