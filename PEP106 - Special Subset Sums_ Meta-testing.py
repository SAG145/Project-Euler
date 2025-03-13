import copy

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

def disjoint(lst1,lst2):
    lst = lst1 + lst2
    return len(list(dict.fromkeys(lst))) == len(lst)

def test(set1,set2):
    larger = set1[0] > set2[0]
    for i in range(1,len(set1)):
        if (set1[i] > set2[i]) != larger:
            return True
    return False

subsets_by_len = [[],[],[],[],[],[],[]]
lst = [1,2,3,4,5,6,7,8,9,10,11,12]
for s in subgroups(lst):
    if len(s) < 7:
        subsets_by_len[len(s)].append(s)
pairs = 0
for set_len in range(2,7):
    for i in range(1,len(subsets_by_len[set_len])):
        for j in range(i):
            if disjoint(subsets_by_len[set_len][i],subsets_by_len[set_len][j]):
                if test(subsets_by_len[set_len][i],subsets_by_len[set_len][j]):
                    pairs += 1
print(pairs)

#Answer = 21384

