pyramidal_probability = [0]*37
cube_probability = [0]*37
for p1 in range(1,5):
    for p2 in range(1, 5):
        for p3 in range(1, 5):
            for p4 in range(1, 5):
                for p5 in range(1, 5):
                    for p6 in range(1, 5):
                        for p7 in range(1, 5):
                            for p8 in range(1, 5):
                                for p9 in range(1, 5):
                                    p = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9
                                    pyramidal_probability[p] += 1/4**9
for c1 in range(1,7):
    for c2 in range(1, 7):
        for c3 in range(1, 7):
            for c4 in range(1, 7):
                for c5 in range(1, 7):
                    for c6 in range(1, 7):
                        c = c1 + c2 + c3 + c4 + c5 + c6
                        cube_probability[c] += 1/6**6
final_probability = 0
for d1 in range(9,37):
    s = 0
    for d2 in range(6,d1):
        s += cube_probability[d2]
    final_probability += s*pyramidal_probability[d1]
print(round(final_probability*10**7)/10**7)

#answer = 0.5731441