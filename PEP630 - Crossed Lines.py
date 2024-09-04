from fractions import Fraction
def line(p,q):
    a,b,c,d = p[0],p[1],q[0],q[1]
    if a == c:
        return (3.1415926535,a)
    m = Fraction(d - b,c - a)
    return (m,b - m*a)

def Ln(n):
    points = []
    m1 = 50515093
    m2 = 2000
    S = [290797]
    T = [S[0] % 2000 - 1000]
    for k in range(1,2*n + 1):
        S.append(S[-1]**2 % 50515093)
        T.append(S[-1] % 2000 - 1000)
        if k % 2 == 0:
            points.append((T[-2],T[-1]))

    lines = []
    for i in range(1,len(points)):
        for j in range(i):
            lines.append(line(points[i],points[j]))
    return sorted(list(dict.fromkeys(lines)))

def S(L):
    print(perf_counter() - start)
    slopes = []
    i = 0
    while i < len(L):
        t = L[i][0]
        j = i
        while i < len(L) and L[i][0] == t:
            i += 1
        slopes.append(i - j)

    inter = 0
    for s in slopes:
        inter += s*(len(L) - s)
    return inter

print(S(Ln(2500)))

#answer = 9669182880384
#זמן הרצה - דקה וחצי