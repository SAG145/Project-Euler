import math

def all_primes_below_n(n):
    primes_bool = [False, False] + [True] * (n - 2)
    for k in range(2, int(math.sqrt(n)) + 1):
        if primes_bool[k]:
            for l in range(2*k,n,k):
                primes_bool[l] = False
    partitions_primes = []
    for k in range(n):
        if primes_bool[k]:
            partitions_primes.append(0)
        else:
            partitions_primes.append(-1)
    return (primes_bool,partitions_primes)

def special_partitions(primes,partis,current_parti,numbers,limit,i3,i2):
    if primes[sum(current_parti)] and (i2 == len(numbers)):
        partis[sum(current_parti)] += 1
    if i2 != len(numbers):
        m = 0
        if i2 == 0:
            m = 2
        for i in range(m,min(i3, len(numbers[i2]))):
            if sum(current_parti) + numbers[i2][i] > limit - 1:
                break
            if i == 0:
                special_partitions(primes,partis,current_parti,numbers,limit,i3,i2 + 1)
            else:
                special_partitions(primes, partis, current_parti + [numbers[i2][i]],numbers,limit,i,i2 + 1)

limit = 10**6
nums_divi_by_2_or_3 = []
for power2 in range(math.floor(math.log(limit,2)) + 1):
    nums = [0]
    for power3 in range(math.floor(math.log(limit // 2**power2,3)) + 1):
        nums.append(3**power3*2**power2)
    nums_divi_by_2_or_3.append(nums)

primes = all_primes_below_n(limit)
partitions = primes[1]
primes_boolean = primes[0]

l = math.floor(math.log(limit,3)) + 2
special_partitions(primes_boolean,partitions,[],nums_divi_by_2_or_3,limit,l,0)
sum1 = 2
for p in range(len(partitions)):
    if partitions[p] == 1:
        sum1 += p
print(sum1)

#Answer = 3053105

#Time: 3:30
