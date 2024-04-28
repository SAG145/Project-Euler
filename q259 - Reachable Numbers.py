import copy
def arith_nums(a,b):
    nums_list = []
    nums_list.append(a + b)
    nums_list.append(a - b)
    nums_list.append(a * b)
    if b != 0:
        nums_list.append(a / b)
    return list(dict.fromkeys(nums_list))

def connect_digits(digits):
    num = ""
    for d in digits:
        num += str(d)
    return int(num)

def minus_lists(lst1,lst2):
    lst = copy.copy(lst1)
    for k in lst2:
        if k in lst:
            lst.remove(k)
    return lst

def sub_to_index(lst,sub):
    sub1 = copy.copy(sub)
    l = len(lst)
    i = 0
    for k in range(len(lst)):
        if lst[k] in sub1:
            sub1.remove(lst[k])
            i += 2**(l - k - 1)
    return i

def subsets(set1):
    subs = []
    for i in range(1,len(set1) + 1):
        for j in range(i):
            subs.append(set1[j:i])
    return subs

def numbers(orig,nums):
    subs1 = subsets(orig)
    subs1.sort(key=len)
    for sub in subs1:
        k = sub_to_index(orig,sub)
        if nums[k] == 0:
            if len(sub) < 2:
                nums[k] = sub
            else:
                sol = []
                for i in range(1,len(sub)):
                    sol1 = nums[sub_to_index(orig,sub[:i])]
                    sol2 = nums[sub_to_index(orig,sub[i:])]
                    for s1 in sol1:
                        for s2 in sol2:
                            sol += arith_nums(s1,s2)
                sol = list(dict.fromkeys(sol))
                nums[k] = sol + [connect_digits(sub)]
    return nums[-1]

def natural_reachable(lst):
    reachable_round = []
    for num in numbers(lst,[0]*2**len(lst)):
        if abs(round(num) - num) < 0.000000001 and round(num) > 0 and num < connect_digits(lst) + 1:
            reachable_round.append(round(num))
    reachable_round = list(dict.fromkeys(reachable_round))
    return sum(reachable_round)


print(natural_reachable([1,2,3,4,5,6,7,8,9]))

#answer = 20101196798