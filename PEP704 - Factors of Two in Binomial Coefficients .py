import math
def S(n):
    l = math.floor(math.log(n,2))
    F_list = [0]*(l + 2)
    s = 1
    p = 1
    while s < 2**l:
        for i in range(1,p):
            F_list[i] += 2**(i - 1)
        p += 1
        s *= 2
    s //= 2
    p -= 1
    b = bin(n + 1)[2:]
    for j in range(1,len(b)):
        if b[j] == "1":
            F_list[j] += 1
            for k in range(1,p - j + 1):
                F_list[j + k] += 2**(k - 1)
    sf = 0
    for f in range(1,len(F_list)):
        sf += F_list[f]*f
    return sf

print(S(10**16))

#answer = 501985601490518144