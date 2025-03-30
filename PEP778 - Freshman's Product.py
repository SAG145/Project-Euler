def u(fresh,opti1,opti2):
    new = [0]*10
    for d1 in range(10):
        for d2 in range(10):
            new[fresh[d1][d2]] += opti1[d1]*opti2[d2]
    return new

def f(fresh,mod,orig,R):
    if R == 1:
        return orig
    t = f(fresh,mod,orig,R // 2)
    opti = u(fresh,t,t)
    if R % 2 == 1:
        opti = u(fresh,opti,orig)
    for i in range(len(opti)):
        opti[i] %= mod
    return opti

def F(R,M):
    fresh = []
    for d1 in range(10):
        fre = []
        for d2 in range(10):
            fre.append(d1*d2 % 10)
        fresh.append(fre)

    origs = []
    for _ in range(len(str(M))):
        origs.append([0]*10)
    for x in range(M + 1):
        i = 0
        while x > 0:
            origs[i][x % 10] += 1
            x //= 10
            i += 1
    s = 0
    for j in range(len(str(M))):
        f1 = f(fresh,10**9 + 9,origs[j],R)
        t = 0
        for d in range(10):
            t += d*f1[d]
        s += t*10**j
    return s % (10**9 + 9)

print(F(234567,765432))

#Answer = 146133880