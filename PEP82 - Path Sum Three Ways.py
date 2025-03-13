def min_path_column(column1,column2):
    len1 = len(column1)
    new_column = []
    for k in range(0,len1):
        mink = column1[k] + column2[k]
        for a in range(0,k):
            mink = min(sum(column1[a:k+1]) + column2[a], mink)
        for b in range(k+1,len1):
            mink = min(sum(column1[k:b+1]) + column2[b], mink)
        new_column.append(mink)
    return new_column

def minimum_path(matrix):
    for k in range(2,len(matrix)+1):
        matrix[-k] = min_path_column(matrix[-k],matrix[-k+1])
    return min(matrix[0])

file = open("0082_matrix.txt").read()
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

column_matrix = []
for k in range(len(matrix)):
    column_matrix.append([])

for i in range(len(matrix)):
    for row in matrix:
        column_matrix[i].append(row[i])
print(minimum_path(column_matrix))

#Answer = 260324

