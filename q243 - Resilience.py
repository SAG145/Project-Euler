import math
def is_prime(n):
    if n % 2 == 0:
        return False
    for k in range(3,int(math.sqrt(n))+1,2):
        if n % k == 0:
            return False
    return True

def prime_factors_without_repetitions(n,primes_list = []):
    if n % 2 == 0:
        if 2 not in primes_list:
            primes_list.append(2)
        return prime_factors_without_repetitions(n / 2, primes_list)
    elif is_prime(n):
        if n not in primes_list:
            primes_list.append(n)
        if 1 in primes_list:
            primes_list.remove(1)
        return primes_list
    else:
        for k in range(3, int(math.sqrt(n)) + 1, 2):
            if n % k == 0:
                if is_prime(k):
                    if k not in primes_list:
                        primes_list.append(k)
                    return prime_factors_without_repetitions(n / k, primes_list)

def euler_function(n):
    mult = n
    list = prime_factors_without_repetitions(n,[])
    for num in list:
        mult *= (1-1/num)
    return int(mult)

def r_func(n):
    return euler_function(n)/(n-1)

a = 15499/94744
print(a)
print(r_func(2*3*5*7*11*13*17*19*23)) #גדול מ a
print(r_func(2*3*5*7*11*13*17*19*23*29)) #קטן מ a
#                       כיוון שעבור כל n שהוא מכפלה של ראשוניים עוקבים (החל מ-2) שכל אחד מהם מופיע בדיוק פעם אחת בפירוק שלו
# הערך של פונקציית אוילר של n הוא מינימום עד n (ולכן גם r_func(n)) הפתרון לשאלה יהיה בין שני המספרים האלה,
#                                                                                    לאחר קצת ניסוי וטעיה מגיעים לפתרון

print(2*2*2*3*5*7*11*13*17*19*23)

#answer = 892371480