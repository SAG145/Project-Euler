def next_turn_chances(chances):
    new = [0]*101
    for k in range(1,100):
        new[k] += chances[k]*1 / 2
        new[k + 1] += chances[k]*2 / 9
        new[k - 1] += chances[k]*2 / 9
        if k == 99:
            new[1] += chances[99]*1 / 36
            new[97] += chances[99]*1 / 36
        elif k == 1:
            new[99] += chances[1]*1 / 36
            new[3] += chances[1]*1 / 36
        else:
            new[k + 2] += chances[k]*1 / 36
            new[k - 2] += chances[k]*1 / 36
    return new

chances = [0]*101
chances[50] = 1
expected_value = 0
for i in range(1,100000):
    chances = next_turn_chances(chances)
    if i > 49:
        expected_value += i*(chances[0] + chances[100])
expected_value = float(str(expected_value)[:12])

print(round(expected_value*10**6) / 10**6)

#answer = 3780.618622