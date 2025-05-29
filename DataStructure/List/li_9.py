#Aliasing and cloning
# slicing
# copy()
li = [10,20,30,40]
# l1 = li[:]
l1 = li.copy()
l1[2] = 98
print(li)
print(l1)