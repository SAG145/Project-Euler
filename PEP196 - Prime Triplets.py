import random
def prob_prime(n):
    for k in range(20):
        if pow(random.randrange(2,n),n - 1,n) != 1:
            return False
    return True

def num_of_primes(lst):
    primes = 0
    for n in lst:
        if prob_prime(n):
            primes += 1
    return primes

def first(row):
    return row*(row - 1) // 2 + 1

def neighbours(n,row,fn,fu,fd):
    ns = []
    i = n - fn
    if row % 2 == 0:
        if fu + i + 1 < fn:
            ns.append(fu + i + 1)
        if fu + i - 1 >= fu:
            ns.append(fu + i - 1)
        ns.append(fd + i)
    else:
        if fd + i - 1 >= fd:
            ns.append(fd + i - 1)
        if fu + i < fn:
            ns.append(fu + i)
        ns.append(fd + i + 1)
    return ns

def S(n):
    pt_sum = 0
    f = first(n)
    fu1 = first(n - 1)
    fu2 = first(n - 2)
    fd1 = first(n + 1)
    fd2 = first(n + 2)
    for k in range(f + 1 - f % 2,fd1,2):
        if prob_prime(k):
            # print(k,k - f,fd1 - k)
            ns1 = neighbours(k,n,f,fu1,fd1)
            if num_of_primes(ns1) > 1:
                pt_sum += k
            else:
                for nei in ns1:
                    if prob_prime(nei):
                        if nei > k:
                            ns2 = neighbours(nei,n + 1,fd1,f,fd2)
                            ns2.remove(k)
                            if num_of_primes(ns2) > 0:
                                pt_sum += k
                                break
                        else:
                            ns2 = neighbours(nei, n - 1, fu1,fu2,f)
                            ns2.remove(k)
                            if num_of_primes(ns2) > 0:
                                pt_sum += k
                                break
    return pt_sum

print(S(5678027) + S(7208785))

#answer = 322303240771079935
#זמן הרצה - 3 וחצי דקות