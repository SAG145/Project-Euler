import copy
import random

def min_index(lst):
    i = 0
    m = lst[0]
    for j in range(1,len(lst)):
        if lst[j] < m:
            m = lst[j]
            i = j
    return i

def zero_indexes(lst):
    zi = []
    for i in range(len(lst)):
        if lst[i] == 0:
            zi.append(i)
    return zi

def min_max_len(lst,m):
    if m == "min":
        l = 1000
        for i in range(len(lst)):
            if len(lst[i]) > 0 and len(lst[i]) < l:
                l = len(lst[i])
        return l % 1000
    l = 0
    for i in range(len(lst)):
        if len(lst[i]) > l:
            l = len(lst[i])
    return l

def assi_zeros(assigned,zeros_rows,final_assi):
    m = min_max_len(zeros_rows,"min")
    for i in range(len(zeros_rows)):
        if not assigned[0][i] and len(zeros_rows[i]) == m:
            j = 0
            while not assigned[0][i] and j < len(zeros_rows[i]):
                r = random.randint(0,len(zeros_rows[i]) - 1)
                if not assigned[1][zeros_rows[i][r]]:
                    final_assi.append((i,zeros_rows[i][r]))
                    assigned[0][i] = True
                    assigned[1][zeros_rows[i][r]] = True
                    zeros_rows[i] = []
                else:
                    zeros_rows[i].pop(j)

def assignment(rows):
    assigned = [[False]*len(rows)] + [[False]*len(rows)]
    zeros_rows = []
    final_assi = []
    for i in range(len(rows)):
        zeros_rows.append(zero_indexes(rows[i]))
    r = 0
    while False in assigned[0] and min_max_len(zeros_rows,"max") > 0:
        assi_zeros(assigned,zeros_rows,final_assi)
        r += 1

    assi = []
    for j in range(len(zeros_rows)):
        if not assigned[0][j]:
            assi.append(j)
    return (assi,final_assi)

def minus_min_rows(rows,columns):
    for i in range(len(rows)):
        mi = min_index(rows[i])
        mini = rows[i][mi]
        for j in range(len(rows[i])):
            rows[i][j] -= mini
            columns[j][i] -= mini

def minus_min_columns(rows,columns):
    for i in range(len(columns)):
        mi = min_index(columns[i])
        mini = columns[i][mi]
        for j in range(len(columns[i])):
            columns[i][j] -= mini
            rows[j][i] -= mini

def minimal_lines(rows):
    assi = assignment(rows)
    rm = assi[0]
    cm = []
    change = False
    v = 0
    while change or v == 0:
        change = False
        v = 1
        for i in range(len(rows)):
            for r in rm:
                if i not in cm and rows[r][i] == 0:
                    cm.append(i)
                    change = True
                    break
        for a in assi[1]:
            if a[0] not in rm and a[1] in cm:
                rm.append(a[0])
                change = True
    brm = []
    bcm = []
    for i in range(len(rows)):
        if not i in rm:
            brm.append(True)
        else:
            brm.append(False)
        if i in cm:
            bcm.append(True)
        else:
            bcm.append(False)
    return (brm,bcm)

def solution(rows,columns):
    minus_min_rows(rows,columns)
    assi = assignment(copy.deepcopy(rows))
    if len(assi[0]) == 0:
        return assi[1]
    minus_min_columns(rows, columns)
    assi = assignment(copy.deepcopy(rows))
    if len(assi[0]) == 0:
        return assi[1]
    v = 0
    while True > 0:
        w = assignment(copy.deepcopy(rows))
        if len(w[0]) == 0:
            return w[1]
        change = False
        v += 1
        ml = minimal_lines(copy.deepcopy(rows))
        mini = 10**10
        for i in range(len(rows)):
            for j in range(len(rows)):
                if not ml[0][i] and not ml[1][j] and rows[i][j] < mini:
                    mini = rows[i][j]

        for i in range(len(rows)):
            for j in range(len(rows)):
                if ml[0][i] and ml[1][j]:
                    rows[i][j] += mini
                    columns[j][i] += mini
                    change = True
                elif not ml[0][i] and not ml[1][j]:
                    rows[i][j] -= mini
                    columns[j][i] -= mini
                    change = True
    return assignment(copy.deepcopy(rows))[1]

file = open("0345_matrix.txt","r").read()
file += " "
rows1 = []
columns1 = []
for i in range(15):
    rows1.append([])
    columns1.append([])
nums = 0
curr_num = ""
for ch in file:
    if ch == " " or ch == "\n":
        if len(curr_num) > 0:
            rows1[nums // 15].append(int(curr_num))
            columns1[nums % 15].append(int(curr_num))
            curr_num = ""
            nums += 1
    else:
        curr_num += ch

new_rows = []
new_columns = []
m = 0
for r in rows1:
    for e in r:
        if e > m:
            m = e

for r in rows1:
    new_row = []
    for e in r:
        new_row.append(-e + m)
    new_rows.append(new_row)

for c in columns1:
    new_column = []
    for e in c:
        new_column.append(-e + m)
    new_columns.append(new_column)

matrix_sum = 0
for s in sorted(solution(new_rows,new_columns)):
    matrix_sum += rows1[s[0]][s[1]]

print(matrix_sum)

#Answer = 13938
