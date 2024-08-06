x = 0
a = 10**15
minus = 10**7*(10**7 + 1)*(2*10**7 + 1) // 6
mod = 10**9
for k in range(1,10**8 + 1):
    n = a // k
    x = (x - minus + n*(n + 1)*(2*n + 1) // 6) % mod
for n in range(1,10**7 + 1):
    x = (x + (a // n)*n**2) % mod
print(x)

#answer = 281632621
