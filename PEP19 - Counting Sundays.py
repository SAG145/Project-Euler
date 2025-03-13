class date:
    def __init__(self,days,months,years,today):
        self.__date = [days,months,years]
        self.__day = today

    def tomorrow(self):
        if self.__day == 7:
            self.__day = 1
        else:
            self.__day += 1
        if self.__date[1] == 1 or self.__date[1] == 3 or self.__date[1] == 5 or self.__date[1] == 7 or self.__date[1] == 8 or self.__date[1] == 10 or self.__date[1] == 12:
            if self.__date[0] == 31:
                self.__date[0] = 1
                if self.__date[1] == 12:
                    self.__date[1] = 1
                    self.__date[2] += 1
                else:
                    self.__date[1] += 1
            else:
                self.__date[0] += 1
        elif self.__date[1] == 2:
            if self.__date[0] == 29:
                self.__date[0] = 1
                self.__date[1] = 3
            elif self.__date[0] == 28:
                if (self.__date[2] % 4 == 0 and self.__date[2] % 100 != 0) or (self.__date[2] % 4 == 0 and self.__date[2] % 400 == 0):
                    self.__date[0] = 29
                else:
                    self.__date[0] = 1
                    self.__date[1] = 3
            else:
                self.__date[0] += 1
        else:
            if self.__date[0] == 30:
                self.__date[0] = 1
                self.__date[1] += 1
            else:
                self.__date[0] += 1

    def get_day_date(self):
        return self.__date[0]

    def get_date(self):
        return self.__date

    def get_day_in_the_week(self):
        return self.__day

    def __str__(self):
        return "date: " + str(self.__date) + " day in the week: " + str(self.__day)

x = 0
date1 = date(1,1,1900,2)
for k in range(365):
    date1.tomorrow()
while date1.get_date() != [31,12,2000]:
    if date1.get_day_date() == 1:
        if date1.get_day_in_the_week() == 1:
            x += 1
    date1.tomorrow()
print(x)

#Answer = 171

