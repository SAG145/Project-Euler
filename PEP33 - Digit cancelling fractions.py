for a in range(1,10):
    for b in range(1,10):
        if a==b==0:
            None
        else:
            c = (9*a*b)/(10*a-b)
            if c == c//1 and a/b<1 and c<10:
                print("a = ",a, " b = ",b, " c = ",c)

#Answer = 100

