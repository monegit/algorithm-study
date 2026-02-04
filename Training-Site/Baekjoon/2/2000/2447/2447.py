import sys


def star(n):
    if n == 1:
        return ["*"]

    stars = star(n // 3)
    result = []

    for s in stars:
        result.append(s * 3)

    for s in stars:
        result.append(s + " " * (n // 3) + s)

    for s in stars:
        result.append(s * 3)

    return result


N = int(sys.stdin.readline())

print('\n'.join(draw_stars(N)))
