x = 1
for num1 in range(201):
    if num1 < 201:
        for num2 in range(101):
            if num1 + num2 * 2 < 201:
                for num5 in range(41):
                    if num1 + num2 * 2 + num5 * 5 < 201:
                        for num10 in range(21):
                            if num1 + num2 * 2 + num5 * 5 + num10 * 10 < 201:
                                for num20 in range(11):
                                    if num1 + num2 * 2 + num5 * 5 + num10 * 10 + num20 * 20 < 201:
                                        for num50 in range(5):
                                            if num1 + num2 * 2 + num5 * 5 + num10 * 10 + num20 * 20 + num50 * 50  < 201:
                                                for num100 in range(3):
                                                    if num1 + num2 * 2 + num5 * 5 + num10 * 10 + num20 * 20 + num50 * 50 + num100 * 100 == 200:
                                                        x += 1
print(x)
#ans = 73682