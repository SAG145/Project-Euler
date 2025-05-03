import math

# from fractions import Fraction
#
# def maximize(T,G,lst,new):
#     if T > G:
#         a = new[G - 1]
#         b = lst[G]
#         return 2*a*b / (a + b)
#     else:
#         a = new[-1]
#         b = 2
#         return 2*a*b / (a + b)
#
# def g(X):
#     lst = [0,Fraction(4,3)]
#     i = 2
#     while lst[-1] < X:
#         new = [1]
#         for j in range(1,i):
#             new.append(maximize(i,j,lst,new))
#         x = maximize(i,i,lst,new)
#         new.append(x)
#         lst = new
#         i += 1
#     return i - 1

def maximize(n):
    return 2 / (1 + (1 / math.sqrt(math.pi*n)*(1 - 1 / (8*n) + 1 / (128*n**2) + 1 / (1024*n**3))))

def g(x):
    a = 0
    b = 10**9
    while a + 1 != b:
        g1 = maximize((a + b) // 2)
        if g1 > x:
            b = (a + b) // 2
        else:
            a = (a + b) // 2
    return b


print(g(1.9999))

#Answer = 127311223

#I used the functions maximize and g (the first) to generate values of g. Eventually I noticed that:
#maximize(n) = 1 / (1 / 2 + choose(2n,n) / 2^(2n + 1))
#When I replaced 2nCn with an asymptotic approximation, maximize was obtained.