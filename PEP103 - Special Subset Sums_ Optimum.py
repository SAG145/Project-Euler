def subgroups(lst):
    if len(lst) == 1:
        return [lst,[]]
    subg = []
    subs = subgroups(lst[1:])
    subg += subs
    a = [lst[0]]
    for g in subs:
        subg.append(a + g)
    return subg

def is_sss(set):
    sums = []
    minis = [sum(set) + 1]*(len(set) - 1)
    maxis = [0]*(len(set) - 1)
    subs = subgroups(set)
    subs.remove([])
    subs.remove(set)
    for g in subs:
        l = len(g)
        s = sum(g)
        sums.append(s)
        if minis[l - 1] > s:
            minis[l - 1] = s
        if maxis[l - 1] < s:
            maxis[l - 1] = s
    for k in range(len(minis) - 1):
        if maxis[k] > minis[k + 1]:
            return False
    sums = list(dict.fromkeys(sums))
    return len(sums) == 2**len(set) - 2

def rule1(set):
    sums = []
    subs = subgroups(set)
    subs.remove([])
    subs.remove(set)
    for g in subs:
        sums.append((len(g),sum(g)))
    sums = list(dict.fromkeys(sums))
    return len(sums) == 2**len(set) - 2

def new_sss(sss,k):
    sss1 = [k]
    for i in sss:
       sss1.append(i + k)
    return sss1

def all_sss(len1,sss_list):
    if len1 >= len(sss_list):
        sss_len1 = []
        sss = all_sss(len1 - 1,sss_list)
        for sss1 in sss:
            for k in range(1,sss1[-1] + 2):
                new = new_sss(sss1,k)
                if rule1(new):
                    sss_len1.append(new)
        return sss_len1
    return sss_list[len1]

def list_to_string(list1):
    str1 = ""
    for i in list1:
        str1 += str(i)
    return str1

sss_list = [[],[[1],[2],[3]]]
string = ""
min1 = 1000
for sss in all_sss(7,sss_list):
    if sum(sss) < min1:
        if is_sss(sss):
            min1 = sum(sss)
            string = list_to_string(sss)
print(string)

#Answer = 20313839404245
