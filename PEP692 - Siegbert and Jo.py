def sum_fib(fib,i):
    if i <= 0:
        return 0
    return fib[i]

def g(fib,fib_sums,limit,fi):
    if fib[fi] > limit:
        return 0
    if fib[fi] == limit:
        return fib[fi]
    if limit >= fib_sums[fi]:
        s = fib[fi]
        if fib[fi] == 1:
            return 1
        for i in range(fi - 1):
            s += fib[i]*max(1,sum_fib(fib,fi - i - 3))
        return s

fib = [1,2]
fib_sums = [1,2]
for _ in range(100):
    fib.append(fib[-1] + fib[-2])
    fib_sums.append(fib[-1] + fib_sums[-2])

G = 0
for i in range(100):
    G += g(fib,fib_sums,23416728348467685,i)
print(G)

#answer = 842043391019219959