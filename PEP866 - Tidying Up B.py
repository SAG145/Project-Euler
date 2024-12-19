expected = [1,1,6]
for i in range(3,101):
    ex = 0
    for j in range(i):
        ex += expected[j]*expected[i - j - 1]
    ex *= i*(2*i - 1)
    ex //= i
    expected.append(ex)
    
print(expected[-1] % 987654319)

#answer = 492401720
