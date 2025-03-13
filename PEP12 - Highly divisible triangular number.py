import math

def divisors(n):
    divi_list = []
    for i in range(1,int(math.sqrt(n)) + 1):
        if n%i==0:
            divi_list.append(i)
            divi_list.append(n/i)
    return divi_list

def triangle(n):
    return(n*(n-1)/2)

for i in range(1,1000000000000000):
    x = divisors(triangle(i))
    y = len(x)
    if y>500:
        print(triangle(i))
        break

#Answer = 76576500

