import fmcsv
import time
import sys

print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ", len(sys.argv))
print("The arguments are: " , str(sys.argv))

fmcsv.save_json("prods-"+str(time.time())+".json")


