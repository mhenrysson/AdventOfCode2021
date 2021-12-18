import math


def main():
    print("First test: ", first(get_test_input()))
    print("First real: ", first(get_input()))
    print("Second test: ", second(get_test_input()))
    print("Second real: ", second(get_input()))


def first(inputs: str):
    data = [a.split("..") for a in inputs.replace("target area: x=", "").split(", y=")]
    x, y = [[int(n) for n in a] for a in data]
    m = 0
    for yy in range(2 * abs(y[1])):
        my = 0
        h = 0
        for t in range(2 * yy + 200):
            h += yy - t
            my = max(h, my)
            if y[0] <= h <= y[1]:
                m = max(m, my)
    return m


def second(inputs: str):
    data = [a.split("..") for a in inputs.replace("target area: x=", "").split(", y=")]
    x, y = [[int(n) for n in a] for a in data]
    m = set()
    for yy in range(-abs(y[0]), 2 * abs(y[0])):
        h = 0
        for t in range(max(2 * yy, 0) + 200):
            h += yy - t
            if y[0] <= h <= y[1]:
                for xx in range(x[1] + 1):
                    nux = 0
                    for xt in range(t + 1):
                        nux += max(xx - xt, 0)
                    if x[0] <= nux <= x[1]:
                        m.add((xx, yy))
    return len(m)


def get_test_input():
    return "target area: x=20..30, y=-10..-5"


def get_input():
    return "target area: x=56..76, y=-162..-134"


if __name__ == '__main__':
    main()
