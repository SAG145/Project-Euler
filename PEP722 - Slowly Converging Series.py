import math

def scientific_notation(n,r):
    s = str(n)
    return str(round(n / 10**(len(s) - 1),r)) + "e" + str(len(s) - 1)

def E(k,q):
    s = 0
    qn = q
    n = 1
    pre = ""
    while True:
        if n % 1000000 == 0:
            if pre == scientific_notation(s,13):
                break
            pre = scientific_notation(s,13)
        r = round(n**k*qn / (1 - qn))
        if r == 0:
            break
        s += r
        qn *= q
        n += 1
    return scientific_notation(s,12)

print(E(15,1 - 1 / 2**25))

#answer = 3.376792776502e132
#34 minutes