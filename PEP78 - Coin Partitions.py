import math

def divisors_sum(n):
    sum = 0
    for l in range(1,int(math.sqrt(n))+1):
        if n%l==0:
            if l**2 == n:
                sum += l
            else:
                sum += l + n/l
    return int(sum)

def partitions(n,partitions_list,index_list,divi_sum_list):
    sum = 0
    if n == 0:
        return 1
    elif n < index_list[-1] + 1:
        return partitions_list[n]
    for k in range(n):
        sum += partitions(k,partitions_list,index_list,divi_sum_list)*divi_sum_list[n-k]
    return (sum // n)

partitions_list = []
index_list = []
divi_sum_list = []
for n in range(10000001):
    divi_sum_list.append(divisors_sum(n))
    partitions_list.append(partitions(n,partitions_list,index_list,divi_sum_list))
    index_list.append(n)
    if partitions_list[n] % 1000000 == 0:
        print(n)
        break

#Answer = 55374

