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

file = str(open("0105_sets.txt").read()) + "\n"
x = 0
set1 = []
num = ""
for ch in file:
    if ch == ",":
        set1.append(int(num))
        num = ""
    elif ch == "\n":
        set1.append(int(num))
        num = ""
        if is_sss(set1):
            x += sum(set1)
        set1 = []
    else:
        num += ch
print(x)

#answer = 73702
