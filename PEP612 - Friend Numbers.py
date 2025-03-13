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

def search_element(k,lst):
    l = len(lst) // 2
    if lst[0][0] == k:
        return lst[0][1]
    elif lst[l][0] > k:
        return search_element(k,lst[:l])
    else:
        return search_element(k,lst[l:])

def list_to_number(lst):
    s = ""
    for k in lst:
        s += str(k)
    return int(s)

sub_digits = subgroups([1,2,3,4,5,6,7,8,9,0])
sub_digits.sort(key = len)
sub_digits.pop(0)
sub_digits.remove([0])
numbers_digits = []
for sub in sub_digits:
    s = 0
    leni = len(sub)
    for l in range(1,19):
        if 0 in sub:
            s += leni**(l - 1)*(leni - 1)
        else:
            s += leni**l
    for sub_sub in subgroups(sub):
        if sub_sub != [0] and sub_sub != [] and sub_sub != sub:
            s -= search_element(list_to_number(sub_sub),numbers_digits)
    numbers_digits.append((list_to_number(sub),s))
    numbers_digits.sort()

pairs = 0
for i in range(len(numbers_digits)):
    nd1 = numbers_digits[i]
    for j in range(i + 1):
        nd2 = numbers_digits[j]
        s1 = str(nd1[0])
        s2 = str(nd2[0])
        if len(set(s1 + s2)) != len(s1) + len(s2) and nd1[1] != 0 and nd2[1] != 0:
            if i == j:
                pairs += nd1[1]*(nd1[1] - 1) // 2
            else:
                pairs += nd1[1]*nd2[1]

print(pairs % 1000267129)

#Answer = 819963842
