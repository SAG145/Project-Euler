def prime_factors_with_repetitions(n,primes_list): #בעת הקריאה לפונקציה יש להוסיף [] במקום של ה primes_list
    if n % 2 == 0:                                 #אחרת בהפעלה חוזרת הפונקציה לא תפעל
        primes_list.append(2)
        return prime_factors_with_repetitions(n/2,primes_list)
    elif is_prime(n):
        primes_list.append(int(n))
        return primes_list
    else:
        for k in range(3,int(math.sqrt(n))+1,2):
            if n % k == 0:
                if is_prime(k):
                    primes_list.append(k)
                    return prime_factors_with_repetitions(n/k,primes_list)