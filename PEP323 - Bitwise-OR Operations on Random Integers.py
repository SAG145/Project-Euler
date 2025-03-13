def chance_to_1(n):
    return 1 - 2**(-n)

def chance_to_pattern_of_ones(n):
    return chance_to_1(n)**32 - chance_to_1(n - 1)**32

print(chance_to_pattern_of_ones(1))
chance = 0
for n in range(1,100):
    chance += n*chance_to_pattern_of_ones(n)

print(round(chance*10**10) / 10**10)

#Answer = 6.3551758451

