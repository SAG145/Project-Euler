not_super = 0
for m1 in range(1,168):
    for m2 in range(m1):
        a = m1**2 - m2**2
        b = 2*m1*m2
        t = abs(a**2 - b**2)
        s = 2*a*b
        if s*t % 168 != 0:
            not_super += 1

print(not_super)

#זה מראה שבכל מקרה השטח יתחלק ב 6 וב 28 ולכן אין אף משולש כזה
#answer = 0
