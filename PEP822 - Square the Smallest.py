import math

def mini(lst):
    i = 0
    for j in range(1,len(lst)):
        if lst[j] < lst[i]:
            i = j
    return i

def maxi(lst):
    i = 0
    for j in range(1,len(lst)):
        if lst[j] > lst[i]:
            i = j
    return i

def S(n,m):
    lst = []
    for i in range(2,n + 1):
        lst.append([round(math.log(math.log(i,1.001),1.001),12),0])
    plus = math.log(2,1.001)
    while True:
        ni = mini(lst)
        xi = maxi(lst)
        if round(lst[xi][0] - lst[ni][0],12) < plus:
            break
        lst[ni] = [round(lst[ni][0] + plus,12),lst[ni][1] + 1]
        m -= 1

    p = m // (n - 1)
    for _ in range(m % (n - 1)):
        ni = mini(lst)
        lst[ni] = [round(lst[ni][0] + plus, 12), lst[ni][1] + 1]
        m -= 1

    s = 0
    for j in range(len(lst)):
        s += pow(j + 2,pow(2,lst[j][1] + p,1234567890),1234567891)

    return s % 1234567891

print(S(10**4,10**16))

#Answer = 950591530
