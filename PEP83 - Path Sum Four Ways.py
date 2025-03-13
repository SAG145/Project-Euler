def update(t,index,new_value):
    lst = list(t)
    lst[index] = new_value
    return tuple(lst)

def min_not_include(t,i):
    min = 10**6 + 0.1
    for index in range(len(t)):
        if i != index:
            if type(t[index]) == int:
                if t[index] < min and t[index] != 0:
                    min = t[index]
    return min

def create_cells(len1,start_cell):
    cells = [(start_cell,start_cell)*2]
    for i in range(1,len1**2):
        if i % len1 == 0:
            if i == len1**2 - len1:
                cells.append((0,0,"n","n"))
            else:
                cells.append((0,0,0,"n"))
        elif i % len1 == len1 - 1:
            if i == len1 - 1:
                cells.append(("n","n",0,0))
            elif i == len1**2 - 1:
                cells.append((0,"n","n",0))
            else:
                cells.append((0,"n",0,0))
        elif i < len1:
            cells.append(("n",0,0,0))
        elif i > len1**2 - len1 - 1:
            cells.append((0,0,"n",0))
        else:
            cells.append((0,0,0,0))
    return cells

def add_value(cells,matrix,len1,previous):
    for c in range(max(0,previous - len1 - 1),len(cells)):
        for i in range(4):
            if cells[c][i] != "n":
                if i == 0:
                    min = min_not_include(cells[c - len1],2)
                elif i == 1:
                    min = min_not_include(cells[c + 1],3)
                elif i == 2:
                    min = min_not_include(cells[c + len1],0)
                else:
                    min = min_not_include(cells[c - 1],1)
                if min != 10**6 + 0.1 and (min + matrix[c] < cells[c][i] or cells[c][i] == 0):
                    cells[c] = update(cells[c],i,min + matrix[c])
                    return c
    return -1

def min_path(matrix,len1):
    cells = create_cells(len1,matrix[0])
    k = 0
    new_cells = 0
    while True:
        new_cells = add_value(cells,matrix,len1,new_cells)
        if new_cells == -1:
            break
        k += 1
    return min_not_include(cells[-1],4)

file = str(open("0083_matrix.txt").read())
matrix = []
current_num = ""
for c in file:
    if c == "," or c == "\n":
        matrix.append(int(current_num))
        current_num = ""
    else:
        current_num += c
print(min_path(matrix,80))

#Answer = 425185

