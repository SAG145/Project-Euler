import math

def is_prime(n):
    if n % 2 == 0 and n != 2:
        return False
    for k in range(3,int(math.sqrt(n))+1,2):
        if n % k == 0:
            return False
    return True

def harshad(list1,n):
    p = 10**(n-1)
    new = []
    for num in list1:
        for d in range(10):
            a = d + num[0]*10
            if a % (num[1] + d) == 0:
                new.append((a,num[1] + d))
    return new

list1 = [[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9)]]
for k in range(2,14):
    lst = harshad(list1[-1],k)
    list1.append(lst)

strong = []
for l in range(1,13):
    s = []
    for h in list1[l]:
        if is_prime(h[0] // h[1]):
            strong.append(h)

x = 0
fdp = [1,3,7,9]
for har in strong:
    for d in fdp:
        if is_prime(10*har[0] + d):
            x += 10*har[0] + d
print(x)

#Answer = 696067597313468

