import math

def prime(n):
    a = True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            a = False
            break
    return a

kmax = 9999
lmax = 9999
i = 0
p = 0
x = 0
for k in range(-1000,1001):
    for l in range(-1000, 1001):
        b = True
        i = 0
        p = 0
        while b:
            n = i*i+k*i+l
            if n<1:
                b = False
            else:
                if prime(n):
                    p += 1
                else:
                    b = False
            i += 1
        if p>x:
            x = p
            kmax = k
            lmax = l
print(kmax*lmax)

#Answer = -59231

