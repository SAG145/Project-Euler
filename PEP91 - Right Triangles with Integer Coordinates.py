import math
def is_right_triangle(dot1,dot2,dot3 = (0,0)):
    d1,d2,d3,d4 = dot1[0],dot1[1],dot2[0],dot2[1]
    a = d1**2+d2**2
    b = d3**2+d4**2
    c = (d1-d3)**2+(d2-d4)**2
    if a + b == c:
        return True
    if a + c == b:
        return True
    if b + c == a:
        return True
    return False

def num_of_right_triangles(n):
    x = 0
    for c10 in range(n+1):
        for c11 in range(n+1):
            for c20 in range(n+1):
                for c21 in range(n+1):
                    c1 = (c10,c11)
                    c2 = (c20,c21)
                    if c1 != (0,0):
                        if c2 != (0,0):
                            if c1 != c2:
                                if is_right_triangle(c1,c2):
                                    x += 1
    return x//2
print(num_of_right_triangles(50))

#answer = 14234
