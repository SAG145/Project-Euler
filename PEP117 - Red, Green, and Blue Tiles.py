def RGB(n,values,index):
    if n == 2:
        return 2
    elif n < 2:
        return 0
    elif n < index + 1:
        return values[n]
    sum = 2 + RGB(n - 1,values,index)
    for k in range(2, 5):
        sum += RGB(n - k,values,index) - 1
    return sum + 1

values = [0,0,2,4,8,15]
index = len(values) - 1
for k in range(index + 1,51):
    values.append(RGB(k,values,index))
    index += 1
print(RGB(50,values,index))

#ansswer = 100808458960497
