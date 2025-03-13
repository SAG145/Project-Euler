import math

def prime(a):
    b = True
    for i in range(2,int(math.sqrt(a))):
        if a%i==0:
            b = False
    return b

for i in range(3,600851475143//2+1,2):
    if 600851475143%i==0 and prime(i):
        print(i)
print("x")

#Answer = 6857

