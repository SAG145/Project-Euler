lst = [0]*10001
lst[9999] = 1111333355557778
lst[9990] = 111333555778
lst[4995] = 111333555778*2
not_find = []
for a in range(1,10001):
    not_find.append(a)
not_find.remove(9999)
not_find.remove(9990)
not_find.remove(4995)
digit_list = ["0","1","2"]
for d1 in digit_list:
    for d2 in digit_list:
        for d3 in digit_list:
            for d4 in digit_list:
                for d5 in digit_list:
                    for d6 in digit_list:
                        for d7 in digit_list:
                            for d8 in digit_list:
                                for d9 in digit_list:
                                    for d10 in digit_list:
                                        for d11 in digit_list:
                                            for d12 in digit_list:
                                                for d13 in digit_list:
                                                    for d14 in digit_list:
                                                        for d15 in digit_list:
                                                            n = int(d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8 + d9 + d10 + d11 + d12 + d13 + d14 + d15)
                                                            if n!= 0:
                                                                i = 0
                                                                while i < len(not_find):
                                                                    if n % not_find[i] == 0:
                                                                        lst[not_find[i]] = n // not_find[i]
                                                                        not_find.pop(i)
                                                                    else:
                                                                        i += 1
print(sum(lst))

#answer = 1111981904675169