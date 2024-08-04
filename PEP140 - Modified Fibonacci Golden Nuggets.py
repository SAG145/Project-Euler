# seq = [0,1,1]
# for k in range(1000):
#     seq.append(seq[-1] + seq[-2])
#
# seq2 = [0,1,4]
# for k in range(1000):
#     seq2.append(seq2[-1] + seq2[-2])
#
# def AG(x):
#     s = 0
#     for i in range(1,1000):
#         s += x**i*seq2[i]
#     return s
#
# def AH(x):
#     s = 0
#     for i in range(1,1000):
#         s += x**i*seq[i - 1]
#     return s
#
# def AF(x):
#     s = 0
#     for i in range(1,1000):
#         s += x**i*seq[i]
#     return s
#
# def eff_AH(p,q):
#     return p**2 / (q**2 - p**2 - p*q)
#
# def funcf(p,q):
#     return p*q / AF(p / q)
#
# def funch(p,q):
#     return p*q / AH(p / q)

def next_sol(sol1,sol2,n):
    a,b,c,d = sol1[0],sol1[1],sol2[0],sol2[1]
    return (a*c + b*d*n,a*d + b*c)

base_sols = [(9,2)]
real_sols = [(14,1),(16,2),(26,5),(34,7),(64,14),(86,19)]
golden_nuggets = []
for i in range(40):
    base_sols.append(next_sol(base_sols[0],base_sols[-1],20))
for j in range(6):
    for bs in base_sols:
        real_sols.append(next_sol(real_sols[j],bs,20))

for rs in real_sols:
    if rs[0] % 10 == 4:
        golden_nuggets.append((rs[0] - 14) // 10)

golden_nuggets.sort()
golden_nuggets.pop(0)
print(sum(golden_nuggets[:30]))

#answer = 5673835352990
#מפיתוח של AG(x) מגלים ש AG(x) = AF(x) + 3AH(x), תוך זמן קצר מצאתי נוסחה ל AH(x) ול AF(x) כבר הייתה לי מ PEP137. בסופו של דבר התקבל ש 5x**2 + 14x + 1 חייב להיות ריבוע שלם ואת זה פתרתי בדומה ל PEP137