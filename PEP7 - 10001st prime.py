import math

def prime(n):
    a = True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            a = False
            break
    return a

prime_list = []
i = 2
while len(prime_list)<10002:
    if prime(i):
        prime_list.append(i)
    i += 1
print(prime_list[10000])

#Answer = 104743
