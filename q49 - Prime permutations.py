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

def contains(str1,str2):
    a = True
    for i in str1:
        if i in str2:
            None
        else:
            a = False
            break
    if a==True:
        for i in str2:
            if i in str1:
                None
            else:
                a = False
                break
    return a

for i in range(1,5000):
    for k in range(1000,10000-2*i):
        if prime(k):
            kstr = str(k)
            if prime(k+i) and contains(kstr,str(k+i)):
                if prime(k+2*i) and contains(kstr,str(k+2*i)):
                    print(k,k+i,k+2*i)
#answer = 296962999629