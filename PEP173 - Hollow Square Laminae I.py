import math

x = 0
def func(n):
    x = 0
    for a in range(1,n//4+1):
        sqrt_delta = int(math.sqrt(a**2+n))
        for b in range(2,sqrt_delta - a + 1,2):
            if b**2 + 2*a*b < n + 1:
                x += 1
                
    return x

print(func(1000000))

#answer = 1572729
