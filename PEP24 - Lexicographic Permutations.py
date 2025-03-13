def repeating_digit(n):
    s = str(n)
    l = len(s)
    for i in range(l):
        for j in range(l):
            if s[i] == s[j]:
                if i != j:
                    return True
    return False

x = 967680
for n in range(2701345689,10**10):
    if repeating_digit(n) == False:
        x += 1
        if x == 1000000:
            print(n)
            break

#Answer = 2783915460
