def same_digits(str1,str2):
    lst1=[]
    lst2=[]
    for i in str1:
        lst1.append(i)
    for j in str2:
        lst2.append(j)
    return sorted(lst1) == sorted(lst2)
i = 1
while 1>0:
    k = str(i)
    if same_digits(k,str(2*i)):
        if same_digits(k,str(3*i)):
            if same_digits(k,str(4*i)):
                if same_digits(k,str(5*i)):
                    if same_digits(k,str(6*i)):
                        print(i)
                        break
    i += 1
#answer = 142857
