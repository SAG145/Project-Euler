import math

def copy(lst):
    lst1 = []
    for i in lst:
        lst1.append(i)
    return(lst1)

def int_str(x):
    if type(x) == int:
        lst = []
        for i in str(x):
            lst.append(int(i))
        return lst
    else:
        a = 0
        for i in range(len(x)):
            a += 10**(len(x) - i-1)*x[i]
        return a

def rotation_int(x):
    lstx = int_str(x)
    lst1 = copy(lstx)
    lst1[len(lstx)-1] = lstx[0]
    for i in range(len(lstx)-1):
        lst1[i] = lstx[i+1]
    return int_str(lst1)

def prime(a):
    b = True
    for i in range(2,int(math.sqrt(a)+1)):
        if a%i==0:
            b = False
    return b

lst1 = []
x = 0
for k in range(2,1000000):
    a = False
    if prime(k):
        p = 0
        a = True
        k2 = k
        while p < len(str(k)) - 1 and a:
            k1 = rotation_int(k2)
            if prime(k1):
                k2 = k1
            else:
                a = False
            p += 1
    if a and "0" not in str(k):
        if k in lst1:
            None
        else:
            lst1.append(k)
            x += 1
print("x = ",x)
#answer = 55
