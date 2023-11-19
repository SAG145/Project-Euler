def b(theta,n):
    if n == 1:
        return theta
    else:
        b1 = b(theta,n-1)
        return int(b1)*(b1 - int(b1) + 1)

def a(theta,n):
    return int(b(theta,n))

def tau(list):
    s = str(list[0]) + "."
    for k in list[1:]:
        s += str(k)
    return s[:26]

#answer = 2.223561019313554106173177
#הגעתי לתשובה על ידי ניסוי ערכים שיצרתי בעזרת הקוד