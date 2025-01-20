def draw(dir):
    if dir == 0:
        return (0,1)
    elif dir == 1:
        return (1,0)
    elif dir == 2:
        return (0,-1)
    else:
        return (-1,0)

def add(t,s):
    return (t[0] + s[0],t[1] + s[1])

def p1(dir):
    return (dir + 1) % 4

def m1(dir):
    return (dir - 1) % 4

def position(pos_list,c,d,steps,dir):
    if steps > 2**d - 1:
        if c == "a":
            return pos_list[0][d][dir]
        return pos_list[1][d][dir]
    if steps <= 0:
        return (0,0)
    if d == 1:
        if c == "a":
            return draw(p1(dir))
        return draw(m1(dir))
    if c == "a":
        if steps <= 2**(d - 1) - 1:
            return position(pos_list,"a",d - 1,steps,dir)
        p = add(position(pos_list,"a",d - 1,steps,dir),position(pos_list,"b",d - 1,steps - 2**(d - 1) + 1,(dir + 3) % 4))
        if steps > 2**d - 2:
            return add(p,draw(p1(dir)))
        return p
    p = add(draw(m1(dir)),position(pos_list,"a",d - 1,steps - 1,m1(dir)))
    if steps <= 2**(d - 1) - 1:
        return p
    return add(p,position(pos_list,"b",d - 1,steps - 2**(d - 1),dir))

pos_list = [[[(0,0)]*4],[[(0,0)]*4]]
for d in range(1,52):
    na = []
    nb = []
    for dir in range(4):
        na.append(add(add(pos_list[0][d - 1][dir],pos_list[1][d - 1][(dir + 3) % 4]),draw(p1(dir))))
        nb.append(add(draw(m1(dir)),add(pos_list[0][d - 1][m1(dir)],pos_list[1][d - 1][dir])))
    pos_list[0].append(na)
    pos_list[1].append(nb)

p = add((0,1),position(pos_list,"a",50,10**12 - 1,0))
print(str(p[0]) + "," + str(p[1]))

#answer = 139776,963904