def f(n):
    mod = 1008691207
    facs = [1]
    sum_facs = [1]
    for i in range(1,n + 1):
        facs.append((facs[-1]*i) % mod)
        sum_facs.append((sum_facs[-1] + facs[-1]) % mod)
    s = facs[n] - 2*sum_facs[n - 1] + 1
    for j in range(1,n // 2 + 1):
        s += 2*sum_facs[n - 2*j] - facs[n - 2*j]
    return s % mod

print(f(10**8))

#Answer = 210286684