import copy
def triangle_3(n):
    return n*(n + 1) // 2

def square_4(n):
    return n**2

def pentagonal_5(n):
    return n*(3*n - 1) // 2

def hexagonal_6(n):
    return n*(2*n - 1)

def heptagonal_7(m):
    return n*(5*n-3) // 2

def octagonal_8(n):
    return n*(3*n-2)

def smart_search_index(lst,elem,index = 0):
    l = len(lst) // 2
    if len(lst) == 0:
        return -1
    if int(lst[l][0]) == elem:
        return index + l
    if int(lst[l][0]) < elem:
        return smart_search_index(lst[l + 1:],elem,index + l + 1)
    else:
        return smart_search_index(lst[:l], elem, index)

def index_starting(start,type):
    lst = all_lst[type - 3]
    i = smart_search_index(lst,int(start))
    if i == -1:
        return range(0,0)
    i1 = i
    i2 = i
    plus = True
    minus = True
    while plus or minus:
        if i2 + 1 == len(lst):
            plus = False
        if i1 == 0:
            minus = False
        if minus:
            if lst[i1 - 1][0] == start:
                i1 -= 1
            else:
                minus = False
        if plus:
            if lst[i2 + 1][0] == start:
                i2 += 1
            else:
                plus = False

    return range(i1,i2 + 1)

lst3,lst4,lst5,lst6,lst7,lst8 = [],[],[],[],[],[]
for n in range(1,150):
    s3,s4,s5,s6,s7,s8 = str(triangle_3(n)),str(square_4(n)),str(pentagonal_5(n)),str(hexagonal_6(n)),str(heptagonal_7(n)),str(octagonal_8(n))
    if len(s3) == 4 and s3[0] != "0" and s3[2] != "0":
        lst3.append((s3[:2],s3[2:],n,3))
    if len(s4) == 4 and s4[0] != "0" and s4[2] != "0":
        lst4.append((s4[:2],s4[2:],n,4))
    if len(s5) == 4 and s5[0] != "0" and s5[2] != "0":
        lst5.append((s5[:2],s5[2:],n,5))
    if len(s6) == 4 and s6[0] != "0" and s6[2] != "0":
        lst6.append((s6[:2],s6[2:],n,6))
    if len(s7) == 4 and s7[0] != "0" and s7[2] != "0":
        lst7.append((s7[:2],s7[2:],n,7))
    if len(s8) == 4 and s8[0] != "0" and s8[2] != "0":
        lst8.append((s8[:2],s8[2:],n,8))

all_lst = [lst3, lst4, lst5, lst6, lst7, lst8]

for a3 in all_lst[0]:
    start_final = a3[0]
    opti3 = copy.copy([4,5,6,7,8])
    for j3 in opti3:
        for i3 in index_starting(a3[1],j3):
            opti4 = copy.copy(opti3)
            opti4.remove(j3)
            a4 = all_lst[j3 - 3][i3]
            for j4 in opti4:
                for i4 in index_starting(a4[1], j4):
                    opti5 = copy.copy(opti4)
                    opti5.remove(j4)
                    a5 = all_lst[j4 - 3][i4]
                    for j5 in opti5:
                        for i5 in index_starting(a5[1], j5):
                            opti6 = copy.copy(opti5)
                            opti6.remove(j5)
                            a6 = all_lst[j5 - 3][i5]
                            for j6 in opti6:
                                for i6 in index_starting(a6[1], j6):
                                    opti7 = copy.copy(opti6)
                                    opti7.remove(j6)
                                    a7 = all_lst[j6 - 3][i6]
                                    for j7 in opti7:
                                        for i7 in index_starting(a7[1], j7):
                                            opti8 = copy.copy(opti7)
                                            opti8.remove(j7)
                                            a8 = all_lst[j7 - 3][i7]
                                            if a8[1] == start_final:
                                                final = [a3[2],a4[2],a5[2],a6[2],a7[2],a8[2]]
                                                if len(set(final)) == len(final):
                                                    final = [a3,a4,a5,a6,a7,a8]
sum = 0
for k in final:
    sum += int(k[0] + k[1])
print(sum)

#answer = 28684
