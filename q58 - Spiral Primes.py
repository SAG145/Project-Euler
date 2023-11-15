import math
def is_prime(n):
    if n == 1:
        return False
    if n % 2 == 0 and n != 2:
        return False
    elif n == 1:
        return False
    for k in range(3,int(math.sqrt(n))+1,2):
        if n % k == 0:
            return False
    return True

n = 1
d = 2
side_length = 1
primes = 0
nums = 1
while True:
    for k in range(1,5):
        # print(n)
        n += d
        if is_prime(n):
            primes += 1
        nums += 1
    d += 2
    side_length += 2
    if primes / nums < 0.1:
        print(side_length)
        break

#answer = 26241