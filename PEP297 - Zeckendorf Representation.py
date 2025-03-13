def sum_zn(bins,fib,fib_sums,limit,fi,elem = 0):
    if limit == fi == 1:
        return elem + 1
    if limit <= 1:
        return elem
    if limit < fib[fi]:
        return elem
    if limit == fib[fi]:
        return 1
    if limit > fib_sums[fi]:
        s = 1
        b = 1
        for i in range(2,fi):
            s += i*bins[i - 1][fi - 2]
            b += bins[i - 1][fi - 2]
        return s + b*elem

    s = 0
    i = 0
    while i < fi - 1 and fib[fi] + fib[i] <= limit:
        s += sum_zn(bins,fib,fib_sums,limit - fib[fi],i,elem + 1)
        i += 1
    return s

def sigma_z(bins,fib,fib_sums,limit):
    s = 0
    for fi in range(1,100):
        s += sum_zn(bins, fib, fib_sums, limit, fi)
    return s

fib = [0,1,2]
fib_sums = [0,1, 2]
for _ in range(100):
    fib.append(fib[-1] + fib[-2])
    fib_sums.append(fib[-1] + fib_sums[-2])

bins = [[0]*100,[*range(100)]]
for i in range(2, 100):
    new = [0]*(2*i - 1)
    for j in range(2*i - 1, 100):
        new.append(bins[-1][j - 2] + new[-1])
    bins.append(new)

print(sigma_z(bins,fib,fib_sums,10**17 - 1))

#Answer = 2252639041804718029
