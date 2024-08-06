import copy
def string(lst_of_sets):
    s = ""
    for set in lst_of_sets:
        for n in set:
            s += str(n)
    return int(s)

def lst_to_sets(lst):
    sorted_sets = []
    sets = [[lst[0], lst[6], lst[7]], [lst[1], lst[7], lst[8]], [lst[2], lst[8], lst[9]], [lst[3], lst[9], lst[5]], [lst[4], lst[5], lst[6]]]
    min_index = 0
    for k in range(1,5):
        if sets[k][0] < sets[min_index][0]:
            min_index = k
    return sets[min_index:] + sets[:min_index]

def same_sum(lst):
    sets = lst_to_sets(lst)
    for k in sets:
        if sum(k) != sum(sets[0]):
            return False
    return True

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

max_string = 0
perm_10 = permutation_1_to_n(9)
for perm in perm_10:
    arrangement = [10] + perm
    if same_sum(arrangement):
        if string(lst_to_sets(arrangement)) > max_string:
            max_string = string(lst_to_sets(arrangement))
print(max_string)

#answer = 6531031914842725
