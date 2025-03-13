def board_print(cells):
    str1 = ""
    for k in range(81):
        if k % 9 == 8:
            str1 += str(cells[k]) + "\n"
        else:
            str1 += str(cells[k]) + " "
    return str1

def copy(lst):
    lst1 = []
    for i in lst:
        lst1.append(i)
    return lst1

def copy_max(lst_of_lst):
    lst1 = []
    for i in lst_of_lst:
        lst1.append(copy(i))
    return lst1

def minimun_index(list1):
    mini = 11
    i = 0
    for k in list1:
        if len(k) < mini and len(k) > 0:
            mini = len(k)
            i = list1.index(k)
    return i

def legal(cells,possibilty_cells):
    for a in range(81):
        number = cells[a]
        if number != "0":
            checklist = lines(a) + columns(a) + blocks(a)
            for c in checklist:
                if cells[c] == number and c != a:
                    return False
        if len(possibilty_cells[a]) == 0 and number == "0":
            return False
    return True

def full(cells):
    for k in cells:
        if k == "0":
            return False
    return True

def lines(cell_num):
    line_lst = []
    start = 9*(cell_num // 9)
    for i in range(9):
        line_lst.append(start + i)
    return line_lst

def columns(cell_num):
    column_lst = []
    start = cell_num % 9
    for i in range(9):
        column_lst.append(start + 9*i)
    return column_lst

def blocks(cell_num):
    blocks_list = [[0, 1, 2, 9, 10, 11, 18, 19, 20], [3, 4, 5, 12, 13, 14, 21, 22, 23], [6, 7, 8, 15, 16, 17, 24, 25, 26], [27, 28, 29, 36, 37, 38, 45, 46, 47], [30, 31, 32, 39, 40, 41, 48, 49, 50], [33, 34, 35, 42, 43, 44, 51, 52, 53], [54, 55, 56, 63, 64, 65, 72, 73, 74], [57, 58, 59, 66, 67, 68, 75, 76, 77], [60, 61, 62, 69, 70, 71, 78, 79, 80]]
    for f in blocks_list:
        for g in f:
            if g == cell_num:
                return f

def solve(cells,possibility_cells):
    if full(cells) and legal(cells,possibility_cells):
        # print(board_print(cells),"hshshshsh")
        return int(cells[0] + cells[1] + cells[2])
    elif not legal(cells,possibility_cells):
        return False
    change = False
    for cell in range(81):
        number = cells[cell]
        if len(possibility_cells[cell]) == 1:
            cells[cell] = possibility_cells[cell][0]
            possibility_cells[cell] = []
            return solve(cells,possibility_cells)
        checklist = lines(cell) + columns(cell) + blocks(cell)
        for a in checklist:
            if number in possibility_cells[a]:
                possibility_cells[a].remove(number)
                change = True
    if change:
        return solve(cells,possibility_cells)
    elif not change:
        minimum = minimun_index(possibility_cells)
        mini_elem = possibility_cells[minimum]
        w = len(mini_elem)
        copy_cells = copy(cells)
        copy_possibility = copy_max(possibility_cells)
        copy_cells[minimum] = copy_possibility[minimum][0]
        copy_possibility[minimum] = []
        v = solve(copy_cells,copy_possibility)
        if v != None and v != False:
            return v
        else:
            possibility_cells[minimum].pop(0)
            return solve(cells,possibility_cells)

file = open("0096_sudoku.txt")
s = file.read()
nums_list = []
cells_list = []
lst1 = []
n_list = ["0","1","2","3","4","5","6","7","8","9"]
i = 0
for k in s:
    if k not in n_list:
        None
    elif s[i-2] == "d" or s[i-3] == "d":
        None
    else:
        nums_list.append(k)
    i += 1
for j in range(4050):
    if (j + 1) % 81 == 0:
        lst1.append(nums_list[j])
        cells_list.append(lst1)
        lst1 = []
    else:
        lst1.append(nums_list[j])

x = 0
for sudoku in cells_list:
    possibility = []
    for k in range(81):
        if sudoku[k] != "0":
            possibility.append([])
        else:
            possibility.append(["1","2","3","4","5","6","7","8","9"])
    solution = solve(sudoku,possibility)
    x += solve(sudoku,possibility)
print(x)

#Answer = 24702

