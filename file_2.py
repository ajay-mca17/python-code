#WAP to check wether a file exist or not.
import os, sys
f = input("Enetr File Name : ")
if(os.path.isfile(f)):
    print("File does exist : ",f)
    fl = open(f,'r')
    print(fl.read())
else:
    print("File Does not exist...")
    sys.exit(0)#Used to terminate the program