def power_mod(base,power,mod):
    if power == 1:
        return base % mod
    a = power_mod(base,power // 2,mod)
    return base**(power % 2)*a**2 % mod