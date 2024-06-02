import copy
from math import factorial
letters = "abcdefghijklmnopqrstuvwxyz"
phrase = "thereisasyetinsufficientdataforameaningfulanswer"
pl = []
lo = []
for l in letters:
    c = 0
    for ch in phrase:
        if ch == l:
            c += 1
    if c != 0:
        pl.append(c)
        lo.append(l)
fac = []
for k in range(50):
    fac.append(factorial(k))
def permutations(lst):
    m = fac[sum(lst)]
    for k in lst:
        m = m // fac[k]
    return m

def options_next_letter(options,pl,word,max_len,i,len1,last):
    if len1 < max_len + 1:
        if last != 0:
            options[0] += permutations(word)
        if len1 != max_len and i < len(pl):
            for k in range(min(pl[i],max_len - len1) + 1):
                if k == 0:
                    options_next_letter(options,pl,word,max_len,i + 1,len1,0)
                else:
                    options_next_letter(options,pl,word + [k],max_len,i + 1,len1 + k,k)

def P(w,l = 15):
    position = [0]
    options_letters = copy.copy(pl)
    for k in range(len(w)):
        m = []
        for i in range(lo.index(w[k])):
            m.append(options_letters[i])
        m = list(dict.fromkeys(m))
        while 0 in m:
            m.remove(0)
        for t in m:
            v = [0]
            new_ol = copy.copy(options_letters)
            new_ol[options_letters.index(t)] -= 1
            options_next_letter(v,new_ol,[],l - k - 1,0,0,0)
            appears = 0
            for j in range(lo.index(w[k])):
                if options_letters[j] == t:
                    appears += 1
            position[0] += appears*(v[0] + 1)
        options_letters[lo.index(w[k])] -= 1
        position[0] += 1
    return position[0]

def correct_letter(letters,options_letters,target,l):
    if len(letters) == 1:
        return (letters[0],P(letters[0],l))
    h = len(letters) // 2
    v = P(letters[h],l)
    if v == target:
        return (letters[h],v)
    if v > target:
        return correct_letter(letters[:h],options_letters,target,l)
    if len(letters) == 2:
        return (letters[1],v)
    return correct_letter(letters[h:],options_letters,target,l)

def W(p):
    word = ""
    options_letters = pl
    l = 15
    while p != 0:
        letters = []
        for let in range(len(lo)):
            if options_letters[let] != 0:
                letters.append(lo[let])
        v = correct_letter(letters,options_letters,p,l)
        word += v[0]
        p -= v[1]
        l -= 1
        options_letters[lo.index(v[0])] -= 1
    return word

print(W(P("legionary") + P("calorimeters") - P("annihilate") + P("orchestrated") - P("fluttering")))

#answer = turnthestarson
#זמן הרצה - שעה