import math

def prime(n):
    a = True
    if n==1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            a = False
            break
    return a

def prime_super_r(n):
    a = True
    while n>0:
        if prime(n):
            None
        else:
            a = False
            break
        n = n//10
    return a

def prime_super_l(n):
    a = True
    while n>0:
        if prime(n):
            None
        else:
            a = False
            break
        n1 = str(n)[1:]
        n = float(n1)
    return a

def contains(lst,str1):
    a = False
    for i in lst:
        if i in str1:
            a = True
            break
    return a

list1 = []
x = 0
i = 10
while len(list1) !=11:
    if prime_super_r(i):
        if prime_super_l(i):
            list1.append(i)
            print(list1)
            x += i
    i += 1
print(x)

#Answer = 748317

