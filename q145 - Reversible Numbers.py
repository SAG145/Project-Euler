def odd_digits(n):
    s = str(n)
    if "0" not in s and "2" not in s and "4" not in s and "6" not in s and "8" not in s:
        return True
    return False

def reverse(n):
    return int(str(n)[::-1])

def reversible(n):
    if n % 10 == 0:
        return False
    if odd_digits(n + reverse(n)):
        return True
    return False

#answer = 608720
#נעזרתי בקוד למעלה ובתוצאות על מספרים קטנים יותר להגיע לתשובה