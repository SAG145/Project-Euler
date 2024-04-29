from math import factorial
def factorial_list(lst):
    m = 1
    for k in lst:
        m *= factorial(k)
    return m

def numbers_to_amounts(nums):
    am = [0]*(nums[-1] + 1)
    for n in nums:
        am[n] += 1
    return am

def first_index_larger(lst,elem,index = 0):
    l = len(lst) // 2
    if len(lst) == 0 or lst[-1][0] <= elem:
        return -1
    if lst[l][0] > elem and (lst[l - 1][0] <= elem or len(lst) == 1):
        return index + l
    if lst[l][0] <= elem:
        return first_index_larger(lst[l + 1:],elem,index + l + 1)
    else:
        return first_index_larger(lst[:l], elem, index)

def all_extra(list1,extra,len1,maxi):
    if len(extra) == len1:
        list1.append(extra)
    else:
        if len(extra) == 0:
            for k in range(1,maxi + 1):
                all_extra(list1, extra + [k], len1, maxi)
        else:
            for k in range(extra[-1],maxi + 1):
                all_extra(list1,extra + [k],len1,maxi)

def num_of_ways_partition(partition,num_of_dice):
    ways = 0
    f = factorial(num_of_dice)
    mini = min(partition)
    extra_dice = num_of_dice - len(partition)
    list1 = []
    all_extra(list1,[],extra_dice,mini)
    for ex in list1:
        ways += f // factorial_list(numbers_to_amounts(ex + partition))
    return ways

def new_summation(n,len1,maxi):
    summ = []
    for p in range(1,n // 2 + 1):
        i = first_index_larger(summations[n - p],p - 0.5)
        if i != -1:
            for k in range(i,len(summations[n - p])):
                new = [p] + summations[n - p][k]
                if len(new) < len1 + 1 and new[-1] < maxi + 1:
                    summ.append(new)
    if n < maxi + 1:
        summ.append([n])
    return summ

summations = [[[0]],[[1]],[[1,1],[2]],[[1,1,1],[1,2],[3]]]
t = 4
while t < 71:
    summations.append(new_summation(t,10,12))
    t += 1

summations1 = summations[-1]
real_summ = []
for summ in summations1:
    if len(summ) == 10:
        real_summ.append(summ)

ways = 0
for part in real_summ:
    ways += num_of_ways_partition(part,20)
print(ways)

#answer = 7448717393364181966