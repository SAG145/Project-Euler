def is_permutation(n1,n2):
    lst1,lst2 = [],[]
    for k in str(n1):
        lst1.append(int(k))
    for j in str(n2):
        lst2.append(int(j))
    return sorted(lst1) == sorted(lst2)
