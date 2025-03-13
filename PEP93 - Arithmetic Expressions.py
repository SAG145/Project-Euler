def arithmatic(lst):
    nums_list = []
    if len(lst) == 2:
        a = lst[0]
        b = lst[1]
        nums_list.append(a+b)
        nums_list.append(abs(a-b))
        nums_list.append(a*b)
        nums_list.append(a/b)
        nums_list.append(b/a)
    elif len(lst) == 3:
        nums_list = []
        a = lst[0]
        b = lst[1]
        c = lst[2]
        x = arithmatic([a,b])
        y = arithmatic([b,c])
        z = arithmatic([a,c])
        for n1 in x:
            nums_list += arithmatic([n1,c])
        for n2 in y:
            nums_list += arithmatic([n2,a])
        for n3 in z:
            nums_list += arithmatic([n3,b])
    else:
        nums_list = []
        a = lst[0]
        b = lst[1]
        c = lst[2]
        d = lst[3]
        x = arithmatic([a,b,c])
        y = arithmatic([b,c,d])
        z = arithmatic([a,c,d])
        w = arithmatic([a,b,d])
        t1 = arithmatic([a,b])
        t2 = arithmatic([a,c])
        t3 = arithmatic([a,d])
        t4 = arithmatic([b,c])
        t5 = arithmatic([b,d])
        t6 = arithmatic([c,d])
        for n1 in x:
            nums_list += arithmatic([n1,d])
        for n2 in y:
            nums_list += arithmatic([n2,a])
        for n3 in z:
            nums_list += arithmatic([n3,b])
        for n4 in w:
            nums_list += arithmatic([n4,c])
        for f1 in t1:
            for f2 in t6:
                nums_list += arithmatic([f1,f2])
        for f3 in t2:
            for f4 in t5:
                nums_list += arithmatic([f3,f4])
        for f5 in t3:
            for f6 in t4:
                nums_list += arithmatic([f5,f6])
    while 0 in nums_list:
        nums_list.remove(0)
    return nums_list

def polishing(list1):
    lst = []
    for m in list1:
        if m % 1 == 0 and m not in lst:
            lst.append(int(m))
    return sorted(lst)

max_len = 0
x = 0
for a in range(1,7):
    for b in range(a+1,8):
        for c in range(b+1,9):
            for d in range(c+1,10):
                s = polishing(arithmatic([a,b,c,d]))
                for tf in range(1,100):
                    if s[tf-1] != tf:
                        if tf > max_len:
                            max_len = tf
                            x = 1000*a + 100*b + 10*c + d
                        break
print(x)

#Answer = 1258

