import math

def prime(n):
    a = True
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i == 0:
            a = False
            break
    return a

def pand(num):
    lst = []
    lst1 = []
    for i in str(num):
        lst.append(int(i))
    for k in range(1,len(str(num))+1):
        lst1.append(k)
    return lst1 == sorted(lst)

x = 0
for i in range (1235,7654322,2):
    if prime(i):
        if pand(i):
            x = i
print(x)

#Answer = 7652413

