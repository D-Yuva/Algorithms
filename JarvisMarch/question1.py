def hullconvex(points):
    leftmost = points[0]

    for point in points:
        if (point[0] < leftmost[0]) or (point[0] == leftmost[0] and point[1] < leftmost[1]):
            leftmost = point
    
    return leftmost

n = int(input())

points = [tuple(map(int, input().split())) for _ in range (n)]


if (n < 3):
    print("Not possible")
else:
    print(hullconvex(points))