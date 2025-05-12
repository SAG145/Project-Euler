import math

def s(iter,c1,c2,c3):
    if iter == 0:
        return 0
    c4 = c1 + c2 + c3 + 2*math.sqrt(abs(c1*c2 + c1*c3 + c2*c3))
    return math.pi / c4**2 + s(iter - 1,c1,c2,c4) + s(iter - 1,c1,c3,c4) + s(iter - 1,c2,c3,c4)

r = 1 / (3 - 2*math.sqrt(3))
s1 = math.pi*r**2
t = s(10,1,1,1) + 3*s(10,1 / r,1,1) + 3*math.pi
print(round((s1 - t) / s1,8))

#Answer = 0.00396087