def gcd(x,y):
    while x % y != 0:
        a = x
        b = y
        y = a % b
        x = b
    return y

def inter(i,j):
    k = lines[i]
    l = lines[j]
    a,b,c = k[0],k[1],k[2]
    d,e,f = l[0],l[1],l[2]
    p1 = (c*e - b*f)
    q1 = (a*e - b*d)
    if p1 == 0 or q1 == 0:
        g1 = 1
    else:
        g1 = gcd(p1,q1)
    p2 = (c*d - a*f)
    q2 = (b*d - a*e)
    if p2 == 0 or q2 == 0:
        g2 = 1
    else:
        g2 = gcd(p2, q2)
    return ((p1 // g1,q1 // g1),(p2 // g2, q2 // g2))

def line(p,q):
    return (p[1] - q[1],q[0] - p[0],q[0]*p[1] - p[0]*q[1])

def larger(n,f):
    return n*f[1] > f[0]

def smaller(n,f):
    return n*f[1] < f[0]

def true_inter(i,j):
    k = lines[i]
    l = lines[j]
    if k[0] == l[0] and k[1] == l[1]:
        return 0
    inter1 = inter(i,j)
    x = inter1[0]
    y = inter1[1]
    si = segments[i]
    sj = segments[j]
    x1,x2 = si[0][0],si[1][0]
    y1,y2 = si[0][1],si[1][1]
    x3,x4 = sj[0][0],sj[1][0]
    y3,y4 = sj[0][1],sj[1][1]
    if (smaller(x1,x) and larger(x2,x)) or (x1 == x2 and smaller(y1,y) and larger(y2,y)):
        if (smaller(x3,x) and larger(x4,x)) or (x3 == x4 and smaller(y3,y) and larger(y4,y)):
            return inter1
    return 0

index = 0
s = [290797]
t = []
segments = []
current_segment = []
lines = []
for k in range(1,20001):
    s.append(s[-1]**2 % 50515093)
    t.append(s[-1] % 500)
    if k % 2 == 0:
        current_segment.append((t[k - 2],t[k - 1]))
    if k % 4 == 0:
        segments.append(tuple(sorted(current_segment)))
        lines.append(line(current_segment[0],current_segment[1]))
        current_segment = []
true_intersection_points = []
for s in range(1,5000):
    for t in range(s):
        i = true_inter(s,t)
        if i != 0:
            true_intersection_points.append(i)
true_intersection_points = list(dict.fromkeys(true_intersection_points))
print(len(true_intersection_points))

#Answer = 2868868

