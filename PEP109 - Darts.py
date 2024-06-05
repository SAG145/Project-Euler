score_list = [0,25,50]
double_list = [50]
for n in range(1,21):
    score_list.append(n)
    score_list.append(2*n)
    score_list.append(3*n)
    double_list.append(2*n)

x = 0
for a in range(63):
    for b in range(a+1):
        for d in double_list:
            if score_list[a] + score_list[b] + d < 100:
                x += 1
print(x)

#answer = 38182
