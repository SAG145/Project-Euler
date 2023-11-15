def digits(n):
    lst = []
    s = str(n)
    for k in s:
        lst.append(int(k))
    return sorted(lst)

def appears(lst1,digits):
    a = 0
    for lst in lst1:
        if lst == digits:
            a += 1
    return a

cubes_digits = []
for k in range(1,100000):
    cubes_digits.append(digits(k**3))

d5 = 0
for d in cubes_digits:
    if appears(cubes_digits,d) == 5:
        d5 = d
        break
for i in range(100000):
    if digits(i**3) == d5:
        print(i**3)
        break

#answer = 127035954683