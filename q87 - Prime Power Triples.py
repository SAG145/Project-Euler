import math
def is_prime(n):
    if n % 2 == 0 and n != 2:
        return False
    for k in range(3,int(math.sqrt(n))+1,2):
        if n % k == 0:
            return False
    return True

square_prime_list = []
cube_prime_list = []
fourth_power_prime_list = []
numbers_list = []
for k in range(2,7072):
    if is_prime(k):
        square_prime_list.append(k**2)
for l in range(2,369):
    if is_prime(l):
        cube_prime_list.append(l**3)
for m in range(2,85):
    if is_prime(m):
        fourth_power_prime_list.append(m**4)

for n1 in fourth_power_prime_list:
    for n2 in cube_prime_list:
        if n1 + n2 < 50000000:
            for n3 in square_prime_list:
                num = n1 + n2 + n3
                if num < 50000000:
                    numbers_list.append(num)

numbers_list = sorted(numbers_list)
final_list = [0]
for k in numbers_list:
    if final_list[-1] != k:
        final_list.append(k)
print(len(final_list)-1)

#answer = 10973443