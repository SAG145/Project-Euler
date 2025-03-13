def power_mod(base,power,mod):
    if power == 1:
        return base % mod
    a = power_mod(base,power // 2,mod)
    return base**(power % 2)*a**2 % mod

def tetration_mod(a,b,mod):
    x = a
    for k in range(b - 1):
        x = power_mod(a,x,mod)
    return x

print(tetration_mod(1777,1855,10**8))

#Answer = 95962097

