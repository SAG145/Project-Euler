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

def squ2_rec_expansions(target,step = 1,num = fraction(1,2)):
    if target == 1:
        return (3,2)
    elif target == step:
        return (num.get_numerator() + num.get_denominator(),num.get_denominator())
    elif target-step>990:
        a = 3136053702171298660676929386435241547904567892311264490855305112724791515048110707218241877136101895941312192018847642118804126536077087128619493316418446409629345245335032746344397659298399421682866675037925402943268686683908934476673646047078107118945595342076824049581450028881910436049495165471396790535992204581587428590909834687730169273606482581789152461737543868019171550
        b = 7571103380112304182814996294822702549959371327330701972466499195651510585982683290443158153011556291130628617792008635235205286835032253129687538852012598130007919911528112161830616689099555166340623468258893180843263203626658524046412640623345542682004568067820278995479747592801990645782760069444507052662702733483015668828390726125386594286220999237963811321178517773192894049
        return squ2_rec_expansions(target,990,fraction(a,b))
    else:
        num1 = fraction(1,1)
        two = fraction(2,1)
        num.plus(two)
        num1.divided(num)
        return squ2_rec_expansions(target,step + 1, num1)
x = 0
for k in range(1,1001):
    squ2k = squ2_rec_expansions(k,1,fraction(1,2))
    if len(str(squ2k[0])) > len(str(squ2k[1])):
        x += 1
print(x)

#answer = 153
