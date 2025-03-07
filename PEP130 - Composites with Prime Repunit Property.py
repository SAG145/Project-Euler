import math

def is_prime(n):
    if n % 2 == 0 and n != 2:
        return False
    for k in range(3,int(math.sqrt(n))+1,2):
        if n % k == 0:
            return False
    return True

def a_function(n):
    power_digit = 1
    num = 1
    while num % n != 0:
        num += 10**power_digit
        power_digit += 1
    return power_digit

sum = 0
num = 0
for n in range(9,100001,2):
    if n % 5 != 0:
        if not is_prime(n):
            if (n-1) % a_function(n) == 0:
                sum += n
                num += 1
                if num == 25:
                    break
print(sum)

#answer = 149253
