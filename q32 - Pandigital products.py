def pand_1_to_9(str):
    lst = []
    for i in str:
        lst.append(int(i))
    return sorted(lst) == [1,2,3,4,5,6,7,8,9]

lst = []
for i in range(1,100):
    for k in range(1,10000):
        m = k*i
        if m in lst:
            None
        else:
            if pand_1_to_9(str(i) + str(k) + str(m)):
                lst.append(m)
x = 0
for s in lst:
    x += s
print(x)
#answer = 45228