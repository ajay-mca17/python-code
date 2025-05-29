#get the information about the list
# len() : total number of element in list
# count() : frequency of a particular elemeent
# index() : return index of a particular element
li = [10,20,30,40,20,60,70,30,20]
l = len(li)
print("Total element : ",l)
freq = li.count(56)
print("Frequncy of element : ",freq)
idx = li.index(300)
print("Index of an element is : ",idx)

