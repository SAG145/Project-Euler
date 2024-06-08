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

def choose(n,k):
    return int(factorial(n)/factorial(k)/factorial(n-k))

def insert(k,lst):
    new = []
    lst1 = [k]
    len1 = len(lst)
    for i in range(len1):
        new.append(lst[:i] + lst1 + lst[i:])
    new.append(lst + lst1)
    return new

def permutation_1_to_n(n):
    if n == 1:
        return [[1]]
    else:
        perm_list = []
        list1 = permutation_1_to_n(n-1)
        for perm in list1:
            perm_list += insert(n,perm)
        return perm_list

def lexi_1(lst):
    lex = 0
    len1 = len(lst) - 1
    for k in range(len1):
        if lst[k + 1] > lst[k]:
            lex += 1
    if lex == 1:
        return True
    return False

def lexi_1_perm(n): #נכתב על סמך בחינה של הערכים שנוצרים מ 2 עד 10 ביצירה יסודית
    if n == 2:
        return 1
    else:
        return 2*lexi_1_perm(n-1) + n - 1

max = 0
for k in range(2,27):
    if choose(26,k)*lexi_1_perm(k) > max:
        max = choose(26,k)*lexi_1_perm(k)
        maxi = k
print(max)

#answer = 409511334375
