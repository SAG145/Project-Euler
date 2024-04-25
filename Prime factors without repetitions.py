def prime_factors_without_repetitions(n,primes_list): #בעת הקריאה לפונקציה יש להוסיף [] במקום של ה primes_list
    if n % 2 == 0:                                    #אחרת בהפעלה חוזרת הפונקציה לא תפעל
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