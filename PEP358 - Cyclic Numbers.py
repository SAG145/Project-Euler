import math

def is_prime(n):
    if n % 2 == 0 and n != 2:
        return False
    for k in range(3,int(math.sqrt(n))+1,2):
        if n % k == 0:
            return False
    return True

def long_division_9(prime):
    sum_of_digits = 0
    nine = prime - 1
    num_of_9 = 0
    current_num = 9
    while num_of_9 < nine:
        new_digit = current_num // prime
        sum_of_digits += new_digit
        current_num = 10*(current_num - prime*new_digit) + 9
        num_of_9 += 1
    return sum_of_digits

# lst = []
# for k in range(72*10**7 + 9891, 73*10**7 + 100,100000):
#     if is_prime(k):
#         lst.append(k)
#         print(k)
#         print(99999999999999999999999 / k) #I used this loop to check which prime numbers p meet the conditions, i.e. 999999... divide by p starting with 137.
#They are greater than 10 to the 8th power, and plus their last five digits multiplied by 56789 modulo 100000 gives 99999, which led to them ending in 09891.
# print(lst[2:])

# print(long_division_9(725509891))
# print(long_division_9(726509891)) #After running the loop, these three numbers came out. I checked each one separately to see if it led to the solution, and in the end I was right.

print(long_division_9(729809891))

#Answer = 3284144505
