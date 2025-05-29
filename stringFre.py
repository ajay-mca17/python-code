def substringFind(str,sub):
    start = count = 0
    while True:
        start = str.find(sub,start)
        if (start == -1):
            break
        count = count + 1
        start = start + 1
    return count
str = "ABCDCDC"
su = "CDC"
print("Occurance = ",substringFind(str,su))