def orientation (p,q,r):
    val = (q[1] - p[1])*(r[0] - q[0]) - (q[0] - p[0])*(r[1] - q[1])

    if val == 0:
        return 0
    elif val > 1:
        return 2
    else:
        return 1
    
def convexHull(points):

    n = len(points)
    leftmost = 0

    if n < 3:
        return []

    for i in range(1, n):
        if (points[i][0] < points[leftmost][0]):
            leftmost = i
        elif (points[i][0] == points[leftmost][0] and points[i][1] < points[leftmost][1]):
            leftmost = i
    
    p = leftmost
    hull = []

    while True:
        hull.append(points[p])

        q = (p+1)%n
        if i in range(n):
            if orientation(points[p], points[i],points[q]) == 2:
                q = i
        
        p = q

        if p == leftmost:
            break
    
    return hull

def main():
    n = int(input())
    points = []
    for _ in range(n):
        x,y = map(int, input().split())
        points.append((x,y))
    
    print(len(convexHull(points)))

if __name__ == "__main__":
    main()