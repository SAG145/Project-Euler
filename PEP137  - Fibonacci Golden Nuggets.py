import math

# fib = [0,1,1]
# for k in range(1000):
#     fib.append(fib[-1] + fib[-2])
#
# def AF(x):
#     s = 0
#     for i in range(1,1000):
#         s += x**i*fib[i]
#     return s

# def func(p,q):
#     return round(p*q / AF(p / q))
#
# def func2(q):
#     d = q - 5
#     return 11 + 9*d + d*(d - 1)
#
# def func5(p):
#     d = 2 - p
#     return 11 + 10*d - d*(d + 1)
#
# def eff_func(p,q):
#     return func2(q) + func5(p) - 11 - (2 - p)*(5 - q)
#
# def sup_eff_func(p,q):
#     return q**2 - p**2 - p*q

def next_sol(sol1,sol2,n):
    a,b,c,d = sol1[0],sol1[1],sol2[0],sol2[1]
    return (a*c + b*d*n,a*d + b*c)

base_sols = [(9,2)]
real_sols = [(22,5),(152,34),(1,2),(1042,233)]
golden_nuggets = []
for i in range(40):
    base_sols.append(next_sol(base_sols[0],base_sols[-1],20))
for j in range(4):
    for bs in base_sols:
        real_sols.append(next_sol(real_sols[j],bs,20))

for rs in real_sols:
    if rs[0] % 10 == 2:
        golden_nuggets.append((rs[0] - 2) // 10)

golden_nuggets.sort()
print(golden_nuggets[14])

#Answer = 1120149658760
#At first I noticed that for p/q it follows that AF(p / q) is also rational and of the form pq/n when n is natural.
# The function func calculates n and its other versions calculate it more simply.
#In the end, it turned out that 5x^2 + 2x + 1 should be a quadratic, and I solved it with Pell's equation.

