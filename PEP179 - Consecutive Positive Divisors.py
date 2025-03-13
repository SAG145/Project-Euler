import math

def divisors(n):
    num_of_divisors = 0
    if int(math.sqrt(n)) == math.sqrt(n):
        num_of_divisors += 1
        for l in range(1,int(math.sqrt(n))):
            if n%l==0:
                num_of_divisors += 2

    else:
        for l in range(1,int(math.sqrt(n)) + 1):
            if n%l==0:
                num_of_divisors += 2
    return num_of_divisors

divi_list = []
for k in range(2,10000001):
    print(k)
    divi_list.append(divisors(k))
x = 0
for i in range(len(divi_list) - 1):
    if divi_list[i] == divi_list[i+1]:
        x += 1
print(x)

#Answer = 986262
#Time: 30:00

