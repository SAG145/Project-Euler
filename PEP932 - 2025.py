def is_2025(n):
    s = str(n)
    l = len(s)
    return s[l // 2] != "0" and ((int(s[:l // 2]) + int(s[l // 2:]))**2 == n or (l > 3 and (int(s[:l // 2 + 1]) + int(s[l // 2 + 1:]))**2 == n))

s = 0
for i in range(4,10**8):
    if is_2025(i**2):
        s += i**2

print(s)

#Answer = 72673459417881349
#Time: 2:30
