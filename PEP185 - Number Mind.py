def insert(str1,index,ch):
    return str1[:index] + str(ch) + str1[index + 1:]

def remove_double_elements(lst):
    i = 0
    new_list = []
    while i < len(lst) - 1:
        if lst[i][0] == lst[i + 1][0]:
            a = lst[i][0]
            while i < len(lst) and lst[i][0] == a:
                i += 1
        else:
            new_list.append(lst[i])
            i += 1
    if lst[-1][0] != lst[-2][0]:
        new_list.append(lst[-1])
    return new_list

def merge_sorted_lists(lst1,lst2):
    new = []
    i = 0
    j = 0
    while i != len(lst1) or j != len(lst2):
        if i == len(lst1):
            new += lst2[j:]
            j = len(lst2)
        elif j == len(lst2):
            new += lst1[i:]
            i = len(lst1)
        elif lst1[i] < lst2[j]:
            new.append(lst1[i])
            i += 1
        else:
            new.append(lst2[j])
            j += 1
    return new

def num_of_correct(num1,num2):
    c = 0
    for i in range(len(num1)):
        if num1[i] == num2[i]:
            c += 1
    return c

def score(guesses,num):
    sc = ""
    for a in guesses[1]:
        sc += str(num_of_correct(a, num))
    for b in guesses[2]:
        sc += str(num_of_correct(b, num))
    for c in guesses[3]:
        sc += str(num_of_correct(c, num))
    return sc

def comp(sc):
    co = ""
    for i in range(6):
        co += str(1 - int(sc[i]))
    for j in range(6,13):
        co += str(2 - int(sc[j]))
    for k in range(13,21):
        co += str(3 - int(sc[k]))
    return co

def overlap(num1,num2,correct):
    digits = 0
    for d in range(16):
        if num1[d] == num2[d]:
            digits += 1
            if digits > correct:
                return False
    return True

def valid(num,guesses):
    for c in range(len(guesses)):
        for guess in guesses[c]:
            if not overlap(num,guess,c):
                return False
    return True

def valids(guesses,scores,num,i,options,si):
    if i == si:
        s = score(guesses,num)
        di = "st"
        if num[0] == "-":
            s = comp(s)
            di = "re"
        scores.append((s,di,num))
    else:
        if num[i] == "-":
            for d in options[i]:
                s = insert(num,i,str(d))
                if valid(s,guesses):
                    valids(guesses,scores,s,i + 1,options,si)
        else:
            valids(guesses,scores,num,i + 1,options,si)

guesses = [["2321386104303845"],["3847439647293047","3174248439465858","8157356344118483","6375711915077050","6913859173121360","4895722652190306"],["5616185650518293","4513559094146117","2615250744386899","6442889055042768","2326509471271448","5251583379644322","2659862637316867"],["5855462940810587","9742855507068353","4296849643607543","7890971548908067","8690095851526254","1748270476758276","3041631117224635","1841236454324589"]]

options = []
for k in range(16):
    op = ["0","1","2","3","4","5","6","7","8","9"]
    op.remove(guesses[0][0][k])
    options.append(op)

starts_scores = []
valids(guesses,starts_scores,"-"*16,0,options,8)
starts_scores.sort()
starts_scores = remove_double_elements(starts_scores)

ends_scores = []
valids(guesses,ends_scores,"-"*16,8,options,16)
ends_scores.sort()
ends_scores = remove_double_elements(ends_scores)

all_scores = merge_sorted_lists(starts_scores,ends_scores)

for i in range(len(all_scores) - 1):
    if all_scores[i][0] == all_scores[i + 1][0]:
        print(all_scores[i][2][8:],all_scores[i + 1][2][:8])

#Answer = 4640261571849533

#Time: 26:00
