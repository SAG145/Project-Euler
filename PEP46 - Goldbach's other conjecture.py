import math

def prime(n):
    a = True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            a = False
            break
    return a

i = 9
while 1>0:
    if prime(i) == False:
        k = 0
        a = False
        while 2*k**2 < i and a == False:
            if prime(i - 2*k**2):
                a = True
            k += 1
        if a == False:
            print(i)
            break
    i += 2

#Answer = 5777

