def base_7(n):
    s = ""
    for pow in range(11,-1,-1):
        s += str(n // 7**pow)
        n -= (n // 7**pow)*7**pow
    return str(int(s))

def tri(n):
    return n*(n + 1) // 2

def num_of_not_divisible(rows):
    b7 = base_7(rows - 1)
    nd_by_7 = 0
    s = 1
    for i in range(len(b7)):
        nd_by_7 += s*tri(int(b7[i]))*28**(len(b7) - i - 1)
        s *= int(b7[i]) + 1
    return nd_by_7 + s

print(num_of_not_divisible(10**9))

#Answer = 2129970655314432
