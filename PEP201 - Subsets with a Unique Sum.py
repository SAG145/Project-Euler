import copy

def next_square(s,sums,sum_limit,len_limit,k):
    new = []
    for sumi in sums:
        new.append(copy.copy(sumi))
    for i in range(sum_limit + 1):
        for j in range(min(len_limit + 1,k)):
            if new[i + s][j + 1] == 0:
                new[i + s][j + 1] += sums[i + s][j + 1]
            new[i + s][j + 1] += sums[i][j]
    return new


def U(A,k):
    sums = [[1] + [0]*k] + [0] * (sum(A))
    for i in range(1,len(sums)):
        sums[i] = [0]*(k + 1)
    sum_limit = 0
    len_limit = 0
    for s in A:
        sums = next_square(s,sums,sum_limit,len_limit,k)
        sum_limit += s
        len_limit += 1

    uniques = []
    for sumi in range(len(sums)):
        if sums[sumi][k] == 1:
            uniques.append(sumi)
    return uniques


S = []
for k in range(1,101):
    S.append(k**2)
print(sum(U(S,50)))

#answer = 115039000
# 3 minutes
