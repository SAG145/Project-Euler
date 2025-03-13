import math

def gcd(x,y):
    while x % y != 0:
        a = x
        b = y
        y = a % b
        x = b
    return y

class fraction:
    def __init__(self,a,b):
        self.__numerator = a
        self.__denominator = b
        g = gcd(a,b)
        self.__numerator = a // g
        self.__denominator = b// g

    def get_numerator(self):
        return self.__numerator

    def get_denominator(self):
        return self.__denominator

    def frac(self):
        return fraction(self.__numerator,self.__denominator)

    def plus(self,other):
        x = self.__numerator
        y = self.__denominator
        a = x
        b = y
        x = a*other.__denominator + b*other.__numerator
        y = b*other.__denominator
        g = gcd(x, y)
        return fraction(x // g, y // g)

    def minus(self,other):
        x = self.__numerator
        y = self.__denominator
        a = x
        b = y
        x = a*other.__denominator - b*other.__numerator
        y = b*other.__denominator
        g = gcd(x, y)
        return fraction(x // g, y // g)

    def divided(self,other):
        x = self.__numerator
        y = self.__denominator
        x *= other.__denominator
        y *= other.__numerator
        g = gcd(x,y)
        return fraction(x // g, y // g)

    def multiple(self,other):
        x = self.__numerator
        y = self.__denominator
        x *= other.__numerator
        y *= other.__denominator
        g = gcd(x, y)
        return fraction(x // g, y // g)

    def value(self):
        return self.__numerator / self.__denominator

def recip(t,n):
    a = t[0]
    b = t[1]
    r = a.multiple(a).multiple(fraction(n,1)).minus(b.multiple(b))
    return (a.divided(r),fraction(0,1).minus(b.divided(r)))

def cf(n):
    a_list = []
    sqrt1 = math.sqrt(n)
    f1 = fraction(1,1)
    f2 = fraction(0,1)
    t = (f1,f2)
    for i in range(100):
        a_list.append(math.floor(sqrt1*t[0].value() + t[1].value()))
        t = (t[0],t[1].plus(fraction(a_list[-1],-1)))
        t = recip(t,n)
        if a_list[-1] == 2*math.floor(sqrt1):
            return a_list

def solution(d):
    sqrt1 = math.floor(math.sqrt(d))
    cf1 = cf(d)[1:]
    period = [sqrt1] + cf1*2
    A = [period[0],period[0]*period[1] + 1]
    l = (len(period) - 1) // 2
    if l % 2 == 0:
        for k in range(2,l):
            A.append(period[k]*A[k - 1] + A[k - 2])
    else:
        for k in range(2,2*l):
            A.append(period[k]*A[k - 1] + A[k - 2])
    return A[-1]

max_s = 0
x = 0
for D in range(2,1001):
    if math.floor(math.sqrt(D))**2 != D:
        s = solution(D)
        if s > max_s:
            max_s = s
            x = D
print(x)

#Answer = 661

