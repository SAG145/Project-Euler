solution_for_n = [0]*100000
for x in range(2,10000):
    for y in range(1,x+1):
        if (x*y) % (x+y) == 0:
            solution_for_n[(x*y)//(x+y)] += 1
            # print(x,y)

print(solution_for_n[1260])
for n in solution_for_n:
    if n > 99:
        print(solution_for_n.index(n))
        break