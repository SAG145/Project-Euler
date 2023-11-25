def CBC(n,values,index):
    if n == 3:
        return 2
    elif n < 3:
        return 0
    elif n < index + 1:
        return values[n]
    sum = n - 2 + CBC(n - 1,values,index)
    for k in range(3, n - 3):
        sum += CBC(n - k - 1,values,index) - 1
    return sum

values = [0,0,0,2]
index = 3
for k in range(4,51):
    values.append(CBC(k,values,index))
    index += 1
print(CBC(50,values,index))

#answer = 16475640049