import math

def prime(n):
    a = True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            a = False
            break
    return a
    
x = 0
for i in range(2,2000000):
    if prime(i):
        x += i
print(x)

# answer = 142913828922
