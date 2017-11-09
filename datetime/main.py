from ferdate import *
import datetime

du1 = DateUtils()
print("Mes dafault es: " + du1.month_name())
print(" mes de 2012-02-03 12:00 es: " + du1.month_name(datetime.datetime(2012,2,3,12,0)))


