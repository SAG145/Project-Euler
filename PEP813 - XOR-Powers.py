def xor_product(a,b):
    p = 0
    bini = bin(b)[2:][::-1]
    for i in range(len(bini)):
        if bini[i] == "1":
            p ^= 2**i*a
    return p

def one_i(s):
    indexes = []
    for i in range(len(s)):
        if s[i] == "1":
            indexes.append(i)
    return indexes

def P(n):
    a = 1
    for _ in range(n):
        a = xor_product(a,11)
    return a

mod = 10**9 + 7
s = P(3**8)
a = 2**52
p = 0
for i in one_i(bin(s)[2:][::-1]):
    p += pow(2,i*a,mod)
print(p % mod)

#Answer = 14063639
