def min_path_row(row1,row2):
    len1 = len(row1)
    for k in range(1,len1+1):
        if k == 1:
            row1[-k] += row2[-k]
        else:
            row1[-k] += min(row2[-k],row1[-k+1])

def minimum_path(matrix):
    len1 = len(matrix[-1])
    for number in range(len1):
        matrix[-1][number] += sum(matrix[-1][number:]) - matrix[-1][number]
    for k in range(2,len(matrix)+1):
        min_path_row(matrix[-k],matrix[-k+1])
    return matrix[0][0]

file = open("0081_matrix.txt").read()
s = str(file)
matrix = []
current_row = []
current_number = ""
for c in s:
    if c == "\n":
        current_row.append(int(current_number))
        matrix.append(current_row)
        current_number = ""
        current_row = []
    elif c == ",":
        current_row.append(int(current_number))
        current_number = ""
    else:
        current_number += c
print(minimum_path(matrix))

#answer = 427337
