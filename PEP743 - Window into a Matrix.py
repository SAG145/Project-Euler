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

k = 10**8
n = 10**16
mod = 10**9 + 7
facs = [1]
inverses = [1]
for i in range(1,k + 1):
    facs.append(i*facs[-1] % mod)
    if i % 2 == 0 or i <= k // 2:
        inverses.append(inverse(facs[-1],mod))
    else:
        inverses.append("")

power = pow(2,n // k,mod)
a = 0
for ones in range(0,k + 1,2):
    a += facs[-1]*inverses[ones]*inverses[(k - ones) // 2]**2*pow(power,ones,mod)

print(a % mod)

#Answer = 259158998

#Time: 10:00
