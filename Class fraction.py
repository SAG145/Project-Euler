class fraction:
    def __init__(self,a,b):
        self.__numerator = a
        self.__denominator = b

    def get_numerator(self):
        return self.__numerator

    def get_denominator(self):
        return self.__denominator

    def plus(self,other):
        x = self.__numerator
        y = self.__denominator
        self.__numerator = x*other.__denominator + y*other.__numerator
        self.__denominator = y*other.__denominator

    def divided (self,other):
        x = self.__numerator
        y = self.__denominator
        self.__numerator *= other.get_denominator()
        self.__denominator *= other.__numerator

    def __str__(self):
        return "fraction = " + str(self.__numerator) + "/" + str(self.__denominator)