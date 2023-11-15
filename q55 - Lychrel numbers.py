def func(n,step_counter=0):
    x1 = str(n)
    x2 = x1[::-1]
    if x1 == x2:
        return step_counter
    elif step_counter>50:
        return 55
    else:
        return func(n + int(x2),step_counter+1)

x = 0
for i in range(10000):
    s = str(i)
    s1 = s[::-1]
    if s == s1:
        if func(i+int(s1)) > 49:
            x += 1
    else:
        if func(i) == 55:
            x += 1
print(x)
#answer = 249