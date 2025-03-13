def gcd(x,y):

    while x % y != 0:

        a = x

        b = y

        y = a % b

        x = b

    return y

def sbe_min(a,b):
    g = gcd(a,b)
    a //= g
    b //= g
    if a == 1:
        return str(b)
    if b == 1:
        return "1," + str(a - 1)
    if a > b:
        q = a // b
        return sbe_min(a % b,b) + "," + str(q)
    q = b // a
    return sbe_min(a,b % a) + "," + str(q)


print(sbe_min(123456789,987654321))

#Answer = 1,13717420,8

