def d12_to_d10(d):
    if d == "A":
        return 10
    if d == "B":
        return 11
    return int(d)

def mp(a,b):
    p = 1
    while b >= a:
        b //= a
        p *= a
    return p

def swap(s,i,j):
    return s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]

def next_perm(s):
    i1 = -1
    i2 = -1
    for j in range(len(s) - 2,-1,-1):
        if s[j] < s[j + 1]:
            i1 = j
            break
    for k in range(len(s) - 1,-1,-1):
        if s[k] > s[i1]:
            i2 = k
            break
    s = swap(s,i1,i2)
    return s[:i1 + 1] + s[i1 + 1:len(s)][::-1]

def b12_to_dec(b12):
    dec = 0
    b12 = b12[::-1]
    for i in range(len(b12)):
        dec += d12_to_d10(b12[i])*12**i
    if len(set(str(dec))) == 10:
        return dec
    return -1

def pandi(dec,base):
    digits = [False]*base
    p = mp(base,dec)
    while dec > 0:
        d = dec // p
        digits[d] = True
        dec -= d*p
        p //= base
    if p > 0:
        digits[0] = True
    return not (False in digits)

def super_pan(b12):
    dec = b12_to_dec(b12)
    if dec != -1:
        if pandi(dec,11):
            for b in range(9,1,-1):
                if not pandi(dec,b):
                    return
            return True
        else:
            return False
    return False

s = "1023456789AB"
super_pans = []
while len(super_pans) != 10:
    if super_pan(s):
        super_pans.append(b12_to_dec(s))
    s = next_perm(s)

print(sum(super_pans))

#Answer = 30510390701978

#Time: 18:00