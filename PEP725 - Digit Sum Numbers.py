from math import factorial
import copy

def partitions(n):
    if n == 1:
        return [[1]]
    p = partitions(n - 1)
    part = []
    for par in p:
        for k in range(len(par)):
            par1 = copy.copy(par)
            par1[k] += 1
            part.append(sorted(par1))
        part.append([1] + par)
    return remove_dup(sorted(part))

def remove_dup(list):
    i = 0
    while i < len(list) - 1:
        if list[i] == list[i + 1]:
            list.pop(i)
        else:
            i += 1
    return list

def factorial_list(list1):
    mult = 1
    for n in list1:
        mult *= factorial(n)
    return mult

def permutations(list):
    return factorial(sum(list)) // factorial_list(list)

def sum_of_DS_part(partition):
    lst = [0] * 10
    for k in partition:
        lst[k] += 1
    lst[0] += 2020 - sum(lst)
    sum1 = 0
    for i in range(10):
        if lst[i] != 0:
            ilst = copy.copy(lst)
            ilst[i] -= 1
            sum1 += permutations(ilst)*a*i
    return sum1

a = int("1"*16)

parti = []
for k in range(1,10):
    parti += partitions(k)
i = 0
for p in parti:
    p.append(sum(p))

sum_ds = 0
for r in parti:
    sum_ds = (sum_ds + sum_of_DS_part(r)) % 10**16
print(sum_ds)

#Answer = 4598797036650685

