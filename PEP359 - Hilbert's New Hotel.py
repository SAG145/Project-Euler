import math

def next(n):
    sqrt1 = math.isqrt(2*n + 1)
    if sqrt1**2 == 2*n + 1:
        return n + 1
    return (sqrt1 + 1)**2 - n

def first_person(f):
    if f < 2:
        return f
    if f % 2 == 0:
        return first_person(f + 1) - f
    h = f // 2
    return 2*h*(h + 1)

def P(f,r):
    if r % 2 == 0:
        return next(P(f,r - 1))
    fp = first_person(f)
    if r == 1:
        return fp

    d = next(next(fp)) - fp
    h = r // 2
    return fp + h*d + 2*h*(h - 1)

t = 71328803586048
s = 0
for p2 in range(28):
    for p3 in range(13):
        f = 2**p2*3**p3
        s += P(f,t // f)

print(s % 10**8)

#Answer = 40632119