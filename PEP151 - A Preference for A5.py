import copy

def num_of_times(lst,elem):
    n = 0
    for k in lst:
        if k == elem:
            n += 1
    return n
single_lst = [0,0,0,0,0,0]

def new_envelope(envelope,single,p,q):
    if num_of_times(envelope,1) == len(envelope):
        single_lst[single] += p / q
    else:
        if len(envelope) == 1:
            single += 1
        en = list(dict.fromkeys(envelope))
        for sheet in en:
            new = copy.copy(envelope)
            p1 = p*num_of_times(envelope,sheet)
            q1 = q*len(envelope)
            if sheet == 1:
                new.remove(1)
                new_envelope(new,single,p1,q1)
            else:
                while sheet != 1:
                    new.remove(sheet)
                    new.append(sheet // 2)
                    new.append(sheet // 2)
                    sheet = sheet // 2
                new.remove(1)
                new_envelope(new,single,p1,q1)

new_envelope([1,2,4,8],0,1,1)
single_average = 0
for s in range(len(single_lst)):
    single_average += s*single_lst[s]
print(round(10**6*single_average / sum(single_lst)) / 10**6)

#answer = 0.464399
