def prob(probs,a,b,t):
    if a > 99:
        return 0
    if b > 99:
        return 1
    return probs[a][b][t]
    
def solve(a,b,c,d):
    y = (c + a*d) / (1 - d*b)
    return (a + b*y,y)

probs = []
for i in range(100):
    new = []
    for j in range(100):
        new.append(["",""])
    probs.append(new)

for p1 in range(99,-1,-1):
    for p2 in range(99,-1,-1):
        mp2 = 0
        mp1 = 0
        for points in range(1,9):
            c = 2**(-points)
            s = solve(c*prob(probs,p1,p2 + 2**(points - 1),0),1 - c,0.5*prob(probs,p1 + 1,p2,1),0.5)
            if s[0] > mp2:
                mp2 = s[0]
                mp1 = s[1]
        probs[p1][p2][0] = mp1
        probs[p1][p2][1] = mp2
        
print(round(probs[0][0][0],8))

#answer = 0.83648556
