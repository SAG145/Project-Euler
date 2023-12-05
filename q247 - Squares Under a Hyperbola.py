import math
def X(corner):
    a = corner[0]
    b = corner[1]
    return 1000000000*(math.sqrt(a**2 + b**2 - 2*a*b +4) - a - b)

def f(corner):
    a = corner[0]
    b = corner[1]
    return (math.sqrt(a**2 + b**2 - 2*a*b + 4) - a - b) / 2

def index_S(n,corners,indexes):
    maxi = 0
    max_x = 0
    max_corner = (0,0)
    max_a = 0
    max_b = 0
    for corner in corners:
        a = corner[0]
        b = corner[1]
        if corner[4] > maxi:
            maxi = corner[4]
            max_corner = corner
            max_a = a
            max_b = b
            max_x = f(max_corner)
    corners.remove(max_corner)
    corners.append((max_a + max_x,max_b,n,"tl",X((max_a + max_x,max_b))))
    corners.append((max_a,max_b + max_x,n,"br",X((max_a,max_b + max_x))))
    n1 = max_corner[2]
    if max_corner[3] == "tl":
        return (indexes[n1][0],indexes[n1][1] + 1)
    else:
        return (indexes[n1][0] + 1, indexes[n1][1])

indexes = [0,(0,0)]
corners = [(1, 0.6180339887498949, 1, 'br', 418113853.0706137), (1.618033988749895, 0, 1, 'tl', 954519992.9480393)]
n = 2
a = 0
while True:
    i = index_S(n,corners,indexes)
    indexes.append(i)
    if i == (3,3):
        a += 1
        if a == 20:
            break
    n += 1

#answer = 782252