import math

def digits_sum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n//10
    return sum

a_list = []
for base in range(2,100):
    for power in range(2,100):
        if digits_sum(base**power) == base:
            a_list.append(base**power)

a_list = sorted(a_list)
print(a_list[29])

#answer = 248155780267521
