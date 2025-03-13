import math

def icbrt(n):
    if cube(n):
        return int(math.cbrt(n))
    cbrt = math.floor(math.cbrt(n))
    if cbrt**3 > n:
        return cbrt - 1
    return cbrt

def cube(n):
    return math.floor(math.cbrt(n))**3 == n

def S(n,s_list,s_cubes):
    if n < 10000:
        return s_list[n]
    cbrt = icbrt(n)
    if cube(n):
        cbrt -= 1
    d = n - cbrt**3
    return d + S(d,s_list,s_cubes) + s_cubes[cbrt]

def D(n):
    if n == 0:
        return 0
    return 1 + D(n - icbrt(n)**3)

def sD(s_list,n):
    if n == 0:
        return 0
    return s_list[n + 1] - s_list[n]

s_cubes = [0,1]
s_list = [0,0,1]
for k in range(2,10**4 + 1):
    d = 1 + sD(s_list,k - icbrt(k)**3)
    s_list.append(s_list[-1] + d)

for k in range(2,icbrt(10**17) + 1):
    s_cubes.append(S(k**3,s_list,s_cubes))

print(S(10**17,s_list,s_cubes))

#Answer = 1105985795684653500
