def plus_lists(lst1,lst2):
    return [lst1[0] + lst2[0],lst1[1] + lst2[1]]

grid = []
for i in range(1000):
    grid.append([True]*1000)

dirs = [[0,1],[1,0],[0,-1],[-1,0]]
curr_dir = 0
poss = [500,500]
last_steps = []
p = -1
bp = 0
num_of_black = 0
ter = -1
while len(last_steps) != ter:
    if p != -1 and (len(last_steps) - p) % 104 == (10**18 - p) % 104:
        ter = len(last_steps) + 104
    if grid[poss[0]][poss[1]]:
        curr_dir = (curr_dir + 1) % 4
    else:
        curr_dir = (curr_dir - 1) % 4
    grid[poss[0]][poss[1]] = not grid[poss[0]][poss[1]]
    if not grid[poss[0]][poss[1]]:
        num_of_black += 1
    else:
        num_of_black -= 1
    last_steps.append(grid[poss[0]][poss[1]])
    poss = plus_lists(poss,dirs[curr_dir])
    if len(last_steps) > 312 and last_steps[-104:] == last_steps[-208:-104] == last_steps[-312:-208] and p == -1:
        p = len(last_steps)
        bp = num_of_black
    if len(last_steps) == p + 104 and p != -1:
        d = num_of_black - bp

print((10**18 - len(last_steps)) // 104*12 + num_of_black)

#Answer = 115384615384614952