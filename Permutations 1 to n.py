def insert(k,lst):
    new = []
    lst1 = [k]
    len1 = len(lst)
    for i in range(len1):
        new.append(lst[:i] + lst1 + lst[i:])
    new.append(lst + lst1)
    return new

def permutation_1_to_n(n):
    if n == 1:
        return [[1]]
    else:
        perm_list = []
        list1 = permutation_1_to_n(n-1)
        for perm in list1:
            perm_list += insert(n,perm)
        return perm_list