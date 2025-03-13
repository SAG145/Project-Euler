def gcd(x,y):
    while x % y != 0:
        a = x
        b = y
        y = a % b
        x = b
    return y

x = 0
fractions_list = []
for d in range(2,12001):
    for n in range(d//3,d//2+2):
        if gcd(n,d) == 1:
            if n/d < 1/2:
                if n/d > 1/3:
                    x += 1
print(x)

#Answer = 7295372

