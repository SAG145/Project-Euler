def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n - 1)

def factorial_list(list):
    mult = 1
    for k in list:
        mult *= factorial(k)
    return mult

def chance(colours):
    c = factorial(50)
    for colour in colours:
        c *= factorial(10) / factorial(10 - colour)
    return c / factorial(70)

lst = [0.0]*6
for purple in range(11):
    for blue in range(11):
        for indigo in range(min(11,21 - purple - blue)):
            for green in range(min(11, 21 - purple - blue - indigo)):
                for yellow in range(min(11, 21 - purple - blue - indigo - green)):
                    for orange in range(min(11, 21 - purple - blue - indigo - green - yellow)):
                        for red in range(min(11, 21 - purple - blue - indigo - green - yellow - orange)):
                            colours = [purple, blue, indigo, green, yellow, orange, red]
                            if sum(colours) == 20:
                                num_of_colours = 0
                                for colour in colours:
                                    if colour != 0:
                                        num_of_colours += 1
                                lst[num_of_colours - 2] += chance(colours)*factorial(20) / factorial_list(colours)
expect = 0
for k in range(len(lst)):
    expect += lst[k] * (k + 2)
print(float(str(expect / sum(lst))[:11]))

#answer = 6.818741802
