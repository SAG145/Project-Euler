import math
digits = [6,2,5,5,4,5,6,3,7,6]
only_mult = [0]
simple = [0]
def simple_digits(n):
    match = 0
    while n > 0:
        match += digits[n % 10]
        n = n // 10
    return match

target = 10**6
for n in range(1,target + 1):
    mini = simple_digits(n)
    simple.append(mini)
    for d in range(2,math.isqrt(n) + 1):
        if n % d == 0:
            v = only_mult[d] + only_mult[n // d] + 2
            if v < mini:
                mini = v
    only_mult.append(mini)

all_cells = []
all = [0]
for i in range(37):
    all_cells.append([])
for n in range(1,target + 1):
    mini = only_mult[n]
    for k in range(2,mini // 2):
        for a in all_cells[k]:
            if a < n:
                if k + all[n - a] + 2 < mini:
                    mini = k + all[n - a] + 2
    all.append(mini)
    all_cells[mini].append(n)

print(sum(all))

#answer = 26688208
#זמן הרצה - 4 וחצי דקות