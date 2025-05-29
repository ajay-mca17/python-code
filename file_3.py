#WAP to read csv file
import csv
f = open("std.csv",'r')
dt = csv.reader(f)
data = list(dt)
for ele in data:
    for data_c in ele:
        print(data_c,'\t\t',end="  ")
    print()