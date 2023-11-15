lst = []
for i in range(1,501):
    lst += [2*i]*4
print(lst)
x = 1
y = 1
for k in lst:
    y += k
    x += y
print(x)
#answer = 669171001