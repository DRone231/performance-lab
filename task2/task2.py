import math
import sys


def read_circle(path):
    with open(path, encoding='utf-8') as f:
        circle = f.read().split()
    for i in range(len(circle)):
        circle[i] = float(circle[i])
    return circle


def read_points(path):
    with open(path, encoding='utf-8') as f:
        points = f.read().split()
    for i in range(len(points)):
        points[i] = float(points[i])
    return points


def circles(circle, points):
    x, y, r = circle
    result = []
    for i in range(0, len(points), 2):
        a = points[i]
        b = points[i+1]
        h = math.sqrt(((x - a)**2)+((y - b)**2))
        if h > r:
            result.append('2')
        elif h == r:
            result.append('0')
        else:
            result.append('1')
    return result


if __name__ == '__main__':
    circle = read_circle(sys.argv[1])
    points = read_points(sys.argv[2])
    res = circles(circle, points)
    print(*res, sep='\n')
