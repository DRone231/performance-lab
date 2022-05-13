import sys


def circle_mas(n, m):
    i = 1
    result = [i]
    while True:
        i += m-1
        i = i % n
        if i == 0:
            i = n
        if i > 1:
            result.append(i)
        elif i == 1:
            break
    return result


if __name__ == '__main__':
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    res = circle_mas(n, m)
    print(*res, sep='')
