import math
def prime(n):
    a = True
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            a = False
            break
    return a

lst = [2]
for i in range(3,48000,2):
    if prime(i):
        lst.append(i)

x = 0
num_x = 0
for i in lst:
    pn = i
    sum = i
    num_p = 1
    num = 2
    n = lst.index(i)
    while sum<1000000 and n<4945:
        sum += lst[n + 1]
        if prime(sum):
            pn = sum
            num = num_p
        num_p += 1
        n += 1
    if num > num_x and pn > x:
        num_x = num
        x = pn
print(x)
#answer = 997651