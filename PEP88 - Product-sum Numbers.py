import math

def log(x,y):
    return math.log(y,int(x))

def multiple(list):
    m = 1
    for k in list:
        m *= k
    return m

def mini(lst):
    if len(lst) == 0:
        return 0
    return min(lst)

def product(limit,min1):
    list = []
    if limit == 1:
        return list
    if min1 == 500 or min1 > limit:
        for k in range(math.floor(log(min1,limit)) + 1):
            list.append([min1]*k)
        return list

    for k in range(math.floor(log(min1,limit)) + 1):
        lst = product(limit / min1**k,min1 + 1)
        for p in lst:
            list.append(p + [min1]*k)
    return list

products = product(30000,2)
products.pop(0)
k = 12000
pk = [[0],[0]]
for i in range(k - 1):
    pk.append([])
for p in products:
    if len(p) != 1:
        m = multiple(p)
        a = m - sum(p) + len(p)
        if a < k + 1:
            pk[a].append(m)
minis = []
for k in pk:
    minis.append(mini(k))
minis = list(dict.fromkeys(minis))
print(sum(minis))

#Answer = 7587457

#The 500 and 30,000 are estimates for the bounds, and they worked.
