def max_path_row(row1,row2):
    len1 = len(row1)
    for k in range(len1):
        row1[k] += max(row2[k],row2[k+1])

def maximum_path(triangle):
    for k in range(2,len(triangle)+1):
        max_path_row(triangle[-k],triangle[-k+1])
    return triangle[0][0]

file = open("0067_triangle.txt").read()
s = str(file)
s = s[:len(s)-1] + "\n"
triangle = []
current_row = []
current_number = ""
for c in s:
    if c == " ":
        current_row.append(int(current_number))
        current_number = ""
    elif c == "\n":
        current_row.append(int(current_number))
        triangle.append(current_row)
        current_number = ""
        current_row = []
    else:
        current_number += c
print(maximum_path(triangle))

#answer = 7273
