def possible_walls(h):
    possibilities = []
    if h % 2 == 0:
        b2 = h // 2
        b3 = 0
    else:
        b2 = h // 2 - 1
        b3 = 1
    while b2 > -1:
        possibilities.append((b2,b3))
        b2 -= 3
        b3 += 2
    walls = []
    numbers = []
    for poss in possibilities:
        list1 = []
        all_choose(list1,min(poss),sum(poss) - 1,0,[])
        i = poss.index(min(poss)) + 2
        j = 2
        if i == 2:
            j = 3
        for p in list1:
            w = []
            for k in range(sum(poss)):
                if k in p:
                    w.append(i)
                else:
                    w.append(j)
            walls.append(w)
            numbers.append(bricks_to_numbers(w))
    return numbers

def all_choose(options,len1,maxi,mini,current_indexes):
    if len(current_indexes) == len1:
        options.append(current_indexes)
    else:
        for i in range(mini,maxi + 1):
            all_choose(options,len1,maxi,i + 1,current_indexes + [i])

def bricks_to_numbers(bricks):
    lst = [0]
    for b in bricks:
        lst.append(lst[-1] + b)
    lst.pop(0)
    lst.pop(-1)
    return lst

def crack_free(s1,s2):
    return len(list(dict.fromkeys(s1 + s2))) != len(s1) + len(s2)

def W(h,v):
    poss_walls = possible_walls(h)
    poss = []
    for i in range(len(poss_walls)):
        poss1 = []
        for j in range(len(poss_walls)):
            if not crack_free(poss_walls[i],poss_walls[j]):
                poss1.append(j)
        poss.append(poss1)
    number_of_options = [1]*len(poss_walls)
    for k in range(v - 1):
        new = [0]*len(poss_walls)
        for wall in range(len(poss_walls)):
            for p in poss[wall]:
                new[p] += number_of_options[wall]
        number_of_options = new
    return sum(number_of_options)

print(W(32,10))

#answer = 806844323190414