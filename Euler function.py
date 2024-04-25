def euler_function(n):
    mult = n
    list = prime_factors_without_repetitions(n,[])
    for num in list:
        mult *= (1-1/num)
    return int(mult)