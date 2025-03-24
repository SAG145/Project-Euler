def extended_Euclid(n,mod):
    if n < mod:
        return extended_Euclid(mod,n)[::-1]
    while n % mod != 0:
        i = extended_Euclid(mod,n % mod)
        q = n // mod
        return (i[1],i[0] - q*i[1])
    return (0,1)

def inverse(n,mod):
    return extended_Euclid(n,mod)[0] % mod

facs = [1]
inverses = [1]
mod = 989898989
for i in range(1,9899):
    facs.append(facs[-1]*i % mod)
    inverses.append(inverse(facs[-1],mod))

s = 0
n = 9898
for i in range(n // 2 + 1):
    j = n // 2 - i
    s = (s + facs[n]*inverses[i]**2*inverses[j]**2) % mod

for a in range(0,n,1):
    for b in range(0,a,1):
        if 5*a - 3*b <= n:
            t = (n - 5*a + 3*b) // 2
            if a + b + 4*(a - b) + t + t == n:
                s = (s + 2*(facs[n]*inverses[a]*inverses[b]*inverses[4*(a - b) + t]*inverses[t])) % mod

print(s)

#Answer = 958666903