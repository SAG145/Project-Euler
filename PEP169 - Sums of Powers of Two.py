def f(n):
    b = bin(n)[2:][::-1]
    num_of_ways_leading_one = 1
    num_of_ways_leading_zero = b.index(("1"))
    b = b[b.index("1") + 1:]
    while len(b) > 0:
        i = b.index("1")
        a = num_of_ways_leading_one + num_of_ways_leading_zero
        num_of_ways_leading_zero = i*num_of_ways_leading_one + (i + 1)*num_of_ways_leading_zero
        num_of_ways_leading_one = a
        b = b[i + 1:]
    return num_of_ways_leading_zero + num_of_ways_leading_one

print(f(10**25))

#Answer = 178653872807
