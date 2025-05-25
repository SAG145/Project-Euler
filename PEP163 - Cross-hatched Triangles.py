import math

def close(a,b):
    if (type(a) == str or type(b) == str) == True and not (a == b == "v"):
        return False
    elif type(a) == float or type(a) == int:
        return abs(a - b) < 10**-8
    else:
        for i in range(len(a)):
            if not close(a[i],b[i]):
                return False
        return True

def round10(a):
    if type(a) == float or type(a) == int:
        return round(a,10)
    else:
        a = list(a)
        for i in range(len(a)):
            a[i] = round10(a[i])
        return tuple(a)

def line(p,q):
    if close(p[0],q[0]):
        return round10(((p[0],),tuple(sorted([p,q]))))
    m = (p[1] - q[1]) / (p[0] - q[0])
    return round10(((m,p[1] - m*p[0]),tuple(sorted([p,q]))))

def mid(A,B):
    return ((A[0] + B[0]) / 2,(A[1] + B[1]) / 2)

def lines(A):
    x,y = A
    B = (x + 0.5,y + math.sqrt(3) / 2)
    C = (x + 1,y)
    return [line(A,B),line(A,C),line(A,mid(B,C)),line(B,C),line(B,mid(A,C)),line(C,mid(A,B))]

def flip_lines(A):
    x, y = A
    B = (x + 0.5, y - math.sqrt(3) / 2)
    C = (x + 1,y)
    return [line(A,mid(B,C)),line(B,mid(A,C)),line(C,mid(A,B))]

def on(a,b,t):
    if a > b:
        return on(b,a,t)
    return a <= t <= b or close(a,t) or close(b,t)

def inter(l1,l2):
    if l1[0][0] == l2[0][0]:
        return -1
    if l1[1][1] == l2[1][1]:
        return l1[1][1]
    if l1[1][0] == l2[1][0]:
        return l1[1][0]
    if len(l2[0]) == len(l1[0]) == 1:
        return -1
    elif len(l2[0]) == 1:
        return inter(l2,l1)
    if len(l1[0]) == 1:
        y = l2[0][0]*l1[0][0] + l2[0][1]
        if on(l1[1][0][1],l1[1][1][1],y) and on(l2[1][0][1],l2[1][1][1],y):
            return (l1[0][0],y)
        else:
            return -1
    else:
        x = (l2[0][1] - l1[0][1]) / (l1[0][0] - l2[0][0])
        if on(l1[1][0][0],l1[1][1][0],x) and on(l2[1][0][0],l2[1][1][0],x):
            return (x,l1[0][0]*x + l1[0][1])
        else:
            return -1


def T(n):
    tlines = []
    for i in range(n):
        for j in range(n - i):
            tlines += lines((0.5*i + j,i*math.sqrt(3) / 2))
            if i > 0:
                tlines += flip_lines((0.5*i + j,i*math.sqrt(3) / 2))
    tlines.sort()
    all_lines = []
    i = 1
    mi = tlines[0][1][0]
    while i < len(tlines):
        if tlines[i][0] != tlines[i - 1][0]:
            all_lines.append((tlines[i - 1][0],(mi,tlines[i - 1][1][1])))
            mi = tlines[i][1][0]
        i += 1
    all_lines.append((tlines[-1][0],(mi,tlines[-1][1][1])))

    inter_lines = []
    for _ in range(len(all_lines)):
        inter_lines.append([-2]*len(all_lines))
    for i in range(1,len(all_lines)):
        for j in range(i):
            inter1 = inter(all_lines[i],all_lines[j])
            inter_lines[i][j] = inter1
            inter_lines[j][i] = inter1
    t = 0
    for i in range(2,len(all_lines)):
        for j in range(1,i):
            if inter_lines[i][j] != -1:
                for k in range(j):
                    if inter_lines[i][k] != -1 and inter_lines[j][k] != -1 and not close(inter_lines[i][k],inter_lines[j][k]):
                        t += 1
    return t

print(T(36))

#Answer = 343047