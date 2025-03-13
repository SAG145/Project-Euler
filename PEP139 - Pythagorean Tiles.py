import math

def gcd(x,y):
    while x % y != 0:
        a = x
        b = y
        y = a % b
        x = b
    return y

def gcd3(a,b,c):
    g1 = gcd(a,b)
    if g1 == 1:
        return 1
    g2 = gcd(b,c)
    return gcd(g1,g2)

pita = []
maxi = 10**8
for m in range(2,math.floor(math.sqrt(maxi)) + 1):
    for n in range(1,m):
        a = m**2 + n**2
        b = 2*m*n
        c = m**2 - n**2
        if a + b + c > maxi - 1:
            break
        if b < c:
            d = c
            c = b
            b = d
        g = gcd3(a,b,c)
        a,b,c = a // g,b // g,c // g
        if a % (b - c) == 0:
            pita.append((a,b,c))

pita = list(dict.fromkeys(pita))
valid_tilling = 0
for p in pita:
    valid_tilling += maxi // sum(p)
print(valid_tilling)

#Answer = 10057761

