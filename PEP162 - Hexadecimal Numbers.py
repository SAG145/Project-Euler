def factorial(n):
    mult = 1
    for k in range(2,n+1):
        mult *= k
    return mult

def choose(n,k):
    return factorial(n)//factorial(k)//factorial(n-k)

def hexi(n,A,one,zero):
    return choose(n-1,zero)*choose(n-zero,one)*choose(n-zero-one,A)*13**(n-zero-one-A)

x = 0
for l in range(3,17):
    for a in range(1,l-1):
        for b in range(1,l-1):
            for c in range(1,l-1):
                if a + b + c < l + 1:
                    x += hexi(l,a,b,c)
print(hex(x)[2:].upper())

#answer = 3D58725572C62302
