import copy

def arith_nums(a,b):
    nums_list = []
    nums_list.append(a + b)
    nums_list.append(abs(a - b))
    nums_list.append(a * b)
    if a % b == 0:
        nums_list.append(a // b)
    if b % a == 0:
        nums_list.append(b // a)
    if 0 in nums_list:
        nums_list.remove(0)
    return list(dict.fromkeys(nums_list))

def sort_subgroups(lst):
    subs = []
    for k in range(2**len(lst)):
        sub = []
        b = bin(k)[2:]
        b = "0"*(len(lst) - len(b)) + b
        for i in range(len(lst)):
            if b[i] == "1":
                sub.append(lst[i])
        subs.append(sub)
    return subs

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

def numbers(orig,nums,set1):
    subs = sort_subgroups(set1)
    subs1 = copy.copy(subs)
    subs1.sort(key=len)
    for sub in subs1:
        k = sub_to_index(orig,sub)
        if nums[k] == 0:
            if len(sub) < 2:
                nums[k] = sub
            else:
                sol = []
                subs_sub = sort_subgroups(sub)
                for i in range(1,len(subs_sub) // 2):
                    sub_sub = subs_sub[i]
                    sol1 = nums[sub_to_index(orig,sub_sub)]
                    sol2 = nums[sub_to_index(orig,minus_lists(sub,sub_sub))]
                    for s1 in sol1:
                        for s2 in sol2:
                            sol += arith_nums(s1,s2)
                sol = list(dict.fromkeys(sol))
                nums[k] = sol
    return nums

def minimum_solution(lst,target):
    minimum = 10000
    subs = sort_subgroups(lst)
    subs1 = copy.copy(subs)
    subs1.sort(key=len)
    nums = [0]*2**len(lst)
    solutions = numbers(lst,nums,lst)
    for k in range(len(solutions)):
        if sum(subs[k]) < minimum:
            if solutions[k] != 0:
                if target in solutions[k]:
                    minimum = sum(subs[k])
    if minimum == 10000:
        return 0
    return minimum

file = str(open("0828_number_challenges.txt").read())
x = 0
challenge = 1
nums = []
current_num = ""
for ch in file:
    if ch == "\n":
        nums.append(int(current_num))
        x = (x + 3**challenge*minimum_solution(nums,target)) % 1005075251
        current_num = ""
        nums = []
        challenge += 1
    elif ch == ":":
        target = int(current_num)
        current_num = ""
    elif ch == ",":
        nums.append(int(current_num))
        current_num = ""
    else:
        current_num += ch
print(x)

#Answer = 148693670

