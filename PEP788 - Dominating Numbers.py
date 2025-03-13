def factorial(n):
    mult = 1
    for k in range(2,n+1):
        mult = (mult*k)
    return mult

def choose(n,k):
    return (factorial(n)//factorial(k)//factorial(n-k)) % 1000000007

def dominating(n):
    sum = 9
    more_than_half = n // 2 + 1
    if n == 1 or n == 2:
        return 9
    for k in range(more_than_half,n):
        sum = (sum + 9*choose(n-1,k-1)*9**(n-k) + choose(n-1,k)*9**(n-k+1)) % 1000000007
    return int(sum)

def D(n):
    sum = 0
    for k in range(1,n + 1):
        print(k)
        sum = (sum + dominating(k)) % 1000000007
        print(sum)
    return sum % 1000000007

print(D(2022))

#Answer = 471745499

#Time: 35:00
