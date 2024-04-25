import math
def divisors_sum(n):
    sum = -n
    for l in range(1,int(math.sqrt(n))+1):
        if n%l==0:
            if l**2 == n:
                sum += l
            else:
                sum += l + n/l
    return int(sum)