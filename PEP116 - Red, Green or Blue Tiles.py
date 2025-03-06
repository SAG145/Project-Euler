def f2(n, v2, i2):
    if n < i2 + 1:
        return v2[n]
    return f2(n - 1, v2, i2) + f2(n - 2, v2, i2) + 1

def f3(n, v3, i3):
    if n < i3 + 1:
        return v3[n]
    return f3(n - 1, v3, i3) + f3(n - 3, v3, i3) + 1

def f4(n, v4, i4):
    if n < i4 + 1:
        return v4[n]
    return f4(n - 1, v4, i4) + f4(n - 4, v4, i4) + 1

i2 = 4
v2 = [0, 0, 1, 2, 4]
i3 = 4
v3 = [0, 0, 0, 1, 2]
i4 = 4
v4 = [0, 0, 0, 0, 1]
for i in range(5, 51):
    v2.append(f2(i, v2, i2))
    v3.append(f3(i, v3, i3))
    v4.append(f4(i, v4, i4))
    i2 += 1
    i3 += 1
    i4 += 1
print(v2[6])

# answer = 20492570929
