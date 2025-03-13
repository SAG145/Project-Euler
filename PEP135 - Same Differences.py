import math

lst1 = [0]*(10**6 + 1)
for b in range(1,10**6):
    for a in range(math.ceil(b / 3),math.floor(1/3*(math.sqrt(4*b**2 + 3000000) - b)) + 1):
        n = 3*a**2 + 2*a*b - b**2
        lst1[n] += 1

num_of_10 = 0
for n in lst1:
    if n == 10:
        num_of_10 += 1
print(num_of_10)

#Answer = 4989

