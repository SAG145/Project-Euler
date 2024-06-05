def line(dot1,dot2):
    x1,y1,x2,y2 = dot1[0],dot1[1],dot2[0],dot2[1]
    if x1 == x2:
        return (0,0)
    m = (y1-y2)/(x1-x2)
    return (m,y1-m*x1)

def contain_origin(triangle):
    dot1,dot2,dot3 = triangle[0],triangle[1],triangle[2]
    line1 = line(dot1,dot2)
    line2 = line(dot2,dot3)
    if line1 == (0,0):
        if dot1[0]*dot3[0] < 0:
            if dot1[1] < dot2[1]:
                line_a = line(dot1,dot3)
                line_b = line(dot2,dot3)
            else:
                line_a = line(dot2,dot3)
                line_b = line(dot1,dot3)
            if line_a[1] < 0 and line_b[1] > 0:
                return True
        return False
    if line2 == (0,0):
        if dot1[0]*dot3[0] < 0:
            if dot3[1] < dot2[1]:
                line_a = line(dot3,dot1)
                line_b = line(dot2,dot1)
            else:
                line_a = line(dot2,dot1)
                line_b = line(dot3,dot1)
            if line_a[1] < 0 and line_b[1] > 0:
                return True
    origin_dot1 = line((0,0),dot1)
    origin_dot3 = line((0,0),dot3)
    if origin_dot1[0] == line2[0] or origin_dot3[0] == line1[0]:
        return False
    x1 = (line2[1] - origin_dot1[1])/(origin_dot1[0] - line2[0])
    x_range_line2 = abs(dot2[0] - dot3[0])
    if abs(x1-dot2[0]) < x_range_line2 and abs(x1-dot3[0]) < x_range_line2:
        x2 = (line1[1] - origin_dot3[1])/(origin_dot3[0] - line1[0])
        x_range_line1 = abs(dot1[0]-dot2[0])
        if abs(x2 - dot2[0]) < x_range_line1 and abs(x2 - dot1[0]) < x_range_line1:
            return True
    return False

file = open('0102_triangles.txt', 'r')
string = str(file.read())
triangles_list = []
coor_str = ""
num_of_coord = 0
triangle = []
for char in string:
    if char == ",":
        if num_of_coord == 5:
            current_y = int(coor_str)
            triangle.append((current_x, current_y))
            triangles_list.append(triangle)
            triangle = []
        elif num_of_coord % 2 == 1:
            current_y = int(coor_str)
            triangle.append((current_x,current_y))
        else:
            current_x = int(coor_str)
        coor_str = ""
        num_of_coord = (num_of_coord + 1) % 6
    elif char == "\n":
        if num_of_coord == 5:
            current_y = int(coor_str)
            triangle.append((current_x, current_y))
            triangles_list.append(triangle)
            triangle = []
        elif num_of_coord % 2 == 1:
            current_y = int(coor_str)
            triangle.append((current_x,current_y))
        else:
            current_x = int(coor_str)
        coor_str = ""
        num_of_coord = (num_of_coord + 1) % 6
    else:
        coor_str += char

x = 0
for t in triangles_list:
    if contain_origin(t):
        x += 1
print(x)

#answer = 228
