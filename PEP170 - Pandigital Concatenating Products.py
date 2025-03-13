import copy
import math

def insert(k,lst):
    new = []
    lst1 = [k]
    len1 = len(lst)
    for i in range(len1):
        new.append(lst[:i] + lst1 + lst[i:])
    new.append(lst + lst1)
    return new

def permutation_0_to_n(n):
    if n == 0:
        return [[0]]
    else:
        perm_list = []
        list1 = permutation_0_to_n(n-1)
        for perm in list1:
            perm_list += insert(n,perm)
        return perm_list

def gcd(x,y):
    if x == 0 or y == 0:
        return 1
    while x % y != 0:
        a = x
        b = y
        y = a % b
        x = b
    return y

def pan(s):
    return len(set(s)) == len(s)

def all_pan_divi(n):
    divi = []
    for k in range(1,math.isqrt(n) + 1,1 + n % 2):
        if n % k == 0:
            if pan(str(k)):
                divi.append(k)
            l = n // k
            if pan(str(l)) and k != l:
                divi.append(l)
    divi.pop(0)
    return divi

def all_splits(found,parts,gcd1,prev_gcd):
    if prev_gcd != 1:
        if len(parts) == 2:
            gcd1 = gcd(int(parts[-1]),int(parts[-2]))
            prev_gcd = parts[0]
        elif len(parts) > 2:
            prev_gcd = gcd(gcd1,int(parts[-2]))
            gcd1 = gcd(prev_gcd,int(parts[-1]))
        if gcd1 != 1 and len(parts) > 1:
            ints = []
            for sp in parts:
                ints.append(int(sp))
            for d in all_pan_divi(gcd1):
                s = str(d)
                for p in ints:
                    s += str(p // d)
                if len(s) == 10 and pan(s):
                    found[0] = 1
        if found[0] == 0 and prev_gcd != 1:
            for i in range(1,len(parts[-1]) - 1):
                new = copy.copy(parts)
                s = new[-1]
                new.pop(-1)
                new.append(s[:i])
                new.append(s[i:])
                all_splits(found,new,gcd1,prev_gcd)

def is_con_prod(s):
    found = [0]
    all_splits(found,[s],0,0)
    if found[0] == 1:
        return True
    return False

pandigitals = sorted(permutation_0_to_n(9))[::-1]
for n in pandigitals:
    s = ""
    for k in n:
        s += str(k)
    if is_con_prod(s):
        print(s)
        break

#Answer = 9857164023

