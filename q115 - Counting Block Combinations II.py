def F(n,min,values,index):
    if n < index + 1:
        return values[n]
    sum = n - min + 1 + F(n - 1,min,values,index)
    for k in range(min, n - min):
        sum += F(n - k - 1,min,values,index) - 1
    return sum

m = 50
values = [0]*m + [2]
index = m
while True:
    values.append(F(index + 1,m,values,index))
    index += 1
    if values[index] > 1000000:
        print(index)
        break

#answer = 168