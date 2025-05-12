import math

def m(r,c,C):
    if r == 0:
        return c
    elif C > c:
        return m(r - 1,c + 1,C)
    t = 2*math.ceil((c - C + 1) / (C - 2)) + 1
    return m(r - 1,t + c,C)

def M(C,R):
    return m(R + 1,0,C)

s = 0
for C in range(3,41):
    s += M(C,30)
print(s)

#Answer = 34315549139516