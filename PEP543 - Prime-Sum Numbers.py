def primes1(n):
    bp = [True]*(n // 2)
    for i in range(1,n + 1):
        j = 1
        while i + j + 2*i*j < len(bp) and j <= i:
            bp[i + j + 2*i*j] = False
            j += 1
    primes = [2]
    for k in range(1,len(bp)):
        if bp[k]:
            primes.append(2*k + 1)
    return primes

def first_index_larger(lst,elem,index = 0):
    l = len(lst) // 2
    if lst[l] > elem and (len(lst) == 1 or lst[l - 1] <= elem):
        return index + l
    if lst[l] <= elem:
        return first_index_larger(lst[l + 1:],elem,index + l + 1)
    else:
        return first_index_larger(lst[:l], elem, index)

def sum2(n):
    if n % 2 == 0:
        return sum2(n + 1) - n // 2
    t = n // 2
    return t*(t + 1)

def S(n,primes):
    pi = first_index_larger(primes,n)
    a = 0
    if primes[pi - 1] == n or primes[pi - 1] == n - 1:
        a = 1
    return sum2(n) - n - (n + 1) // 2 + 2 + 2*pi - a

fib = [0,1,1]
for _ in range(42):
    fib.append(fib[-1] + fib[-2])

primes = primes1(fib[-1] + 1000)
s = 0
for i in range(3,len(fib)):
    s += S(fib[i],primes)

print(s)

#Answer = 199007746081234640
#Time: 14:00
