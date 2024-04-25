def pandigital_1_to_9(n): #הקלט צריך להיות מספר תשע ספרתי
    s = str(n)
    for k in range(1,10):
        if str(k) not in s:
            return False
    return True