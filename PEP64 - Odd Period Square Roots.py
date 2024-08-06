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
    while True:
        a_list.append(math.floor(sqrt1*t[0].value() + t[1].value()))
        t = (t[0],t[1].plus(fraction(a_list[-1],-1)))
        t = recip(t,n)
        if a_list[-1] == 2*math.floor(sqrt1):
            return a_list


odd = 0
for N in range(2,10000):
    if math.floor(math.sqrt(N))**2 != N:
        if len(cf(N)) % 2 == 0:
            odd += 1
print(odd)

#answer = 1322
