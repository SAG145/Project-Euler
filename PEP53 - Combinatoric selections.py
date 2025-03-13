def factorial(n,mult = 1):
    for i in range(1,n+1):
        mult *= i
    return mult

def n_k(n,k):
    return int((factorial(n)/(factorial(k)*factorial(n-k))))

x = 0
for i in range(1,101):
    k = 1
    while k < i:
        if n_k(i,k) > 1000000:
            x += 1
        k += 1
print(x)

#Answer = 4075

