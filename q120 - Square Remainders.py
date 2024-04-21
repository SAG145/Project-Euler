def r(a,n):
    return 2*a*n % a**2

def max_r(a):
    maxi = 0
    for n in range(1,10*a,2):
        if r(a,n) > maxi:
            maxi = r(a,n)
    return maxi

sum1 = 0
for a in range(3,1001):
    sum1 += max_r(a)
print(sum1)

#answer = 333082500