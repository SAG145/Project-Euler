import math

def divisors_sum(n):
    sum = -n
    for l in range(1,int(math.sqrt(n))+1):
        if n%l==0:
            if l**2 == n:
                sum += l
            else:
                sum += l + n/l
    return int(sum)

len_max_chain = 0
minimax = 0
for k in range(10,1000001):
    a = divisors_sum(k)
    len = 1
    min = k
    chain_list = [a,k]
    while a < 1000001:
        if a < min:
            min = a
        if a == k:
            a += 1000001
            if len > len_max_chain:
                minimax = min
                len_max_chain = len
        elif a == 1:
            a += 1000001
        else:
            a0 = divisors_sum(a)
            if a0 in chain_list and a0 != k:
                a = 1000001
            else:
                len += 1
                a = a0
                chain_list.append(a)
print(minimax)

#Answer = 14316

