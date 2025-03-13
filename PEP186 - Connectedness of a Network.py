reps = []
friends_rep = []
for pn in range(10**6):
    reps.append(pn)
    friends_rep.append([pn])
S = [0]
suc_calls = 0
k = 1
mod = 10**6
while len(friends_rep[reps[524287]]) < 990000:
    if k < 56:
        S.append((100003 - 200003 * k + 300007 * k ** 3) % mod)
    else:
        S.append((S[k - 24] + S[k - 55]) % mod)
    if k % 2 == 0:
        cr = S[-2]
        cd = S[-1]
        if cr != cd:
            suc_calls += 1
            if reps[cr] != reps[cd]:
                if len(friends_rep[reps[cr]]) > len(friends_rep[reps[cd]]):
                    for f in friends_rep[reps[cd]]:
                        friends_rep[reps[cr]].append(f)
                    rep1 = reps[cr]
                    rep2 = reps[cd]
                    for g in friends_rep[rep2]:
                        reps[g] = rep1
                    friends_rep[rep2] = -1
                else:
                    for f in friends_rep[reps[cr]]:
                        friends_rep[reps[cd]].append(f)
                    rep1 = reps[cd]
                    rep2 = reps[cr]
                    for g in friends_rep[rep2]:
                        reps[g] = rep1
                    friends_rep[rep2] = -1
    k += 1

print(suc_calls)

#Answer = 2325629
