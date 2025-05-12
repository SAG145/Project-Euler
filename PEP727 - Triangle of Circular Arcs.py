import math
import cmath

def gcd(x,y):
    while x % y != 0:
        a = x
        b = y
        y = a % b
        x = b
    return y

def tan(x):
    return math.tan(math.radians(x))

def A(a,b,c):
    x = (2*b**2 + 2*a*b + 2*b*c - 2*a*c) / (2*(b + c))
    return (x,math.sqrt((a + b)**2 - x**2))

def angle(a,b,c):
    return math.degrees(math.acos((a**2 + b**2 - c**2) / (2*a*b)))

def intersection(l1,l2):
    x = (l2[1] - l1[1]) / (l1[0] - l2[0])
    return (x,l1[0]*x + l1[1])

def D(a,b,c):
    s1,s2,s3 = a + b,a + c,b + c
    ang1 = angle(s1,s3,s2)
    ang2 = angle(s2,s3,s1)
    l1 = (tan(ang1 / 2),0)
    m2 = tan(180 - ang2 / 2)
    l2 = (m2,-m2*(b + c))
    return intersection(l1,l2)

def E(a,b,c):
    c1,c2,c3 = 1 / a,1 / b, 1 / c
    c4 = c1 + c2 + c3 + 2*math.sqrt(abs(c1*c2 + c1*c3 + c2*c3))
    A1 = A(a,b,c)
    z1,z3 = complex(A1[0],A1[1]),b + c
    z4 = (z1*c1 + z3*c3 + 2*cmath.sqrt(c1*c3*z1*z3)) / c4
    return (z4.real,z4.imag)

def d(a,b,c):
    x1,y1 = D(a,b,c)
    x2,y2 = E(a,b,c)
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

triples = 0
s = 0
for a in range(3,101):
    for b in range(2,a):
        for c in range(1,b):
            g = gcd(gcd(a,b),c)
            if g == 1:
                triples += 1
                s += d(a,b,c)

print(round(s / triples,8))

#Answer = 3.64039141