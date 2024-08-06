first_cube = []
def not_equal(lst):
    lst1 = []
    for k in lst:
        if k in lst1:
            return False
        lst1.append(k)
    return True

def minus_lists(lst1,lst2):
    for k in lst2:
        lst1.remove(k)
    return lst1

def copy_lists(lst1,lst2 = []):
    for k in lst1:
        lst2.append(k)
    return lst2

def could_formed(n,lst1,lst2):
    for i in lst1:
        for j in lst2:
            if 10*i + j == n or 10*j + i == n:
                return True
    return False

def sorting_lists_with_equal_len(lst1,lst2):
    len1 = len(lst1)
    for k in range(len1):
        if lst1[k] < lst2[k]:
            bigger = lst2
            smaller = lst1
            break
        elif lst1[k] > lst2[k]:
            bigger = lst1
            smaller = lst2
            break
    return (smaller,bigger)

for n1 in range(0,10):
    for n2 in range(0, 10):
        if not_equal([n1,n2]):
            for n3 in range(0, 10):
                if not_equal([n1,n2,n3]):
                    for n4 in range(0,10):
                        minus_lst = [n1,n2,n3,n4]
                        if not_equal(minus_lst):
                            list1 = minus_lists([0,1,2,3,4,5,6,7,8,9],minus_lst)
                            if list1 not in first_cube:
                                first_cube.append(list1)

second_cube = copy_lists(first_cube)
legal_cubes = []
x = 0
y = 0
for lst1 in first_cube:
    for lst2 in second_cube:
        if could_formed(1,lst1,lst2):
            if could_formed(4, lst1, lst2):
                if could_formed(6, lst1, lst2) or could_formed(9, lst1, lst2):
                    if could_formed(16, lst1, lst2) or could_formed(19, lst1, lst2):
                        if could_formed(25, lst1, lst2):
                            if could_formed(36, lst1, lst2) or could_formed(39, lst1, lst2):
                                if could_formed(64, lst1, lst2) or could_formed(94, lst1, lst2):
                                    if could_formed(81, lst1, lst2):
                                        final_list = sorting_lists_with_equal_len(lst1,lst2)
                                        if final_list not in legal_cubes:
                                            legal_cubes.append(final_list)
print(len(legal_cubes))

#answer = 1217
