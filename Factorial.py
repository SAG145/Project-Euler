def factorial(n):
    if n == 0:
        return 1
    else:
        if n % 2 == 0:
            mult = n*(n//2)
            for k in range(1,n//2):
                mult *= k*(n-k)
            return mult
        else:
            mult = n
            for k in range(1,n//2+1):
                mult *= k*(n-k)
            return mult