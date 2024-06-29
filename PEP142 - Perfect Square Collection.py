import math
def perfect_square(n):
    return math.isqrt(n)**2 == n

even_squ = []
odd_squ = []
for k in range(1,1000):
    if k % 2 == 0:
        even_squ.append(k**2)
    else:
        odd_squ.append(k**2)

diff = []
for i in range(1,len(even_squ)):
    for j in range(i):
        mid = (even_squ[i] + even_squ[j]) // 2
        diff.append((mid,mid - even_squ[j]))

for i in range(1,len(odd_squ)):
    for j in range(i):
        mid = (odd_squ[i] + odd_squ[j]) // 2
        diff.append((mid,mid - odd_squ[j]))

diff.sort()

for i in range(len(diff) - 1):
    if diff[i][0] == diff[i + 1][0]:
        if perfect_square(diff[i][1] + diff[i + 1][1]):
            if perfect_square(diff[i + 1][1] - diff[i][1]):
                print(diff[i][0] + diff[i][1] + diff[i + 1][1])
                break