import math

def num_of_latice_points(x,y):
    points = 0
    for a in range(1,x):
        for b in range(1,y):
            if b*x + a*y < x*y:
                points += 1
    return points

def square_lattice_points(m):
    lattice_points = [[0]]
    for x in range(1,m + 1):
        points = [0]
        for y in range(1,m + 1):
            points.append(num_of_latice_points(x,y))
        lattice_points.append(points)

    maxi = 10*lattice_points[-1][-1]
    squares = []
    for n in range(maxi + 1):
        if math.isqrt(n)**2 == n:
            squares.append(True)
        else:
            squares.append(False)

    square_lattice_points = 0
    for a in range(1,m + 1):
        for b in range(1, m + 1):
            points1 = lattice_points[a][b]
            for c in range(1, m + 1):
                points2 = points1 + lattice_points[b][c]
                for d in range(1,m + 1):
                    points_final = points2 + lattice_points[a][d] + lattice_points[c][d] + a + b + c + d - 3
                    if squares[points_final]:
                        square_lattice_points += 1
    return square_lattice_points

print(square_lattice_points(100))

#Answer = 694687

