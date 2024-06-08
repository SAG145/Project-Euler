import math

def tangent_equation(dot):
    x,y = dot[0],dot[1]
    return (-4*x/y,4*x**2/y+y)

def arctan(x):
    return 180/math.pi*(math.atan(x))

def tan(x):
    return math.tan(x*math.pi/180)
def line_equation_between_two_dots(dot1,dot2):
    a, b, c, d = dot1[0], dot1[1], dot2[0], dot2[1]
    m = (b-d)/(a-c)
    return (m,b-m*a)

def next_dot_from_line_and_dot(dot,line):
    m = line[0]
    b = line[1]
    a = dot[0]
    solutions = power_2_equation(4+m**2,2*m*b,b**2-100)
    if float(str(solutions[0])[:10]) == float(str(a)[:10]):
        solution = solutions[1]
    else:
        solution = solutions[0]
    return (solution,m*solution+b)

def power_2_equation(a,b,c):
    discri = b**2-4*a*c
    discri_sqrt = math.sqrt(discri)
    return ((-b+discri_sqrt)/(2*a),(-b-discri_sqrt)/(2*a))

def next_dot_from_two_dots(dot1,dot2):
    a,b,c,d = dot1[0],dot1[1],dot2[0],dot2[1]
    m1 = tangent_equation(dot2)[0]
    m2 = line_equation_between_two_dots(dot1,dot2)[0]
    angle1 = arctan(m1)
    angle2 = arctan(m2)
    angle3 = angle2 - angle1
    angle4 = 180-2*angle3
    angle5 = angle2 + angle4
    m3 = tan(angle5)
    line = (m3,d-m3*c)
    return next_dot_from_line_and_dot(dot2,line)

dot1 = (0,10.1)
dot2 = (1.4,-9.6)
times_beam_hit = 1
while True:
    x = dot2[0]
    if x>-0.01:
        if x<0.01:
            y = dot2[1]
            if y>0:
                print(times_beam_hit-1)
                break
    d1 = dot1
    d2 = dot2
    dot1 = d2
    dot2 = next_dot_from_two_dots(d1,d2)
    times_beam_hit += 1

#answer = 354
