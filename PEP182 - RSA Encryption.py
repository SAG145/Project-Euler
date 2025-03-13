def gcd(x,y):
    while x % y != 0:
        a = x
        b = y
        y = a % b
        x = b
    return y

phi = 1008*3642

mini_sum = 0

for e in range(0,phi):
    if gcd(e,phi) == 1:
        if gcd((e - 1) // 2,phi) == 1:
            mini_sum += e

print(mini_sum)

#Answer = 399788195976
