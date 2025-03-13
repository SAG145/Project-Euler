def Ao(c):
    return 2*(c - 2)**2*(c - 2 + (c - 3)**2) + (c - 1)*(c - 2)*(c - 2 + (c - 3)**2) + (c - 2)**2*(c - 3) + (c - 2)**2*(c - 3)*(2*(c - 2) + (c - 3)*(c - 4))

def Bo(c):
    return (c - 2)**3 + (c - 2)**2*(c - 1 + (c - 3)*(c - 2)) + (c - 2)**4 + (c - 2)**2*(c - 3)*(c - 1 + (c - 3)*(c - 2)) + (c - 1)*(c - 2)**3

def N(a,b,c):
    mod = 10**8
    lst = []
    for _ in range(a + b + 1):
        lst.append([0]*(a + 1))
    lst[1][0] = c*(c - 1)*Bo(c)
    if a > 0:
        lst[1][1] = c*(c - 1)*Ao(c)
    for i in range(1,a + b):
        for j in range(a):
            if i - j < b:
                lst[i + 1][j] += lst[i][j]*Bo(c) % mod
            lst[i + 1][j + 1] += lst[i][j]*Ao(c) % mod
        lst[i + 1][a] += lst[i][a]*Bo(c) % mod
    return sum(lst[a + b]) % mod

print(N(25,75,1984))

#Answer = 61190912

