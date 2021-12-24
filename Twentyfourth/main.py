import math


def main():
    print("First real: ", first(get_input()))
    print("Second real: ", second(get_input()))


def first(inputs: str):
    instructions = [d.splitlines() for d in inputs.split("inp w\n")][1:]
    instructions = [[j.split(" ") for j in i] for i in instructions]
    valid = [{} for i in range(14)]
    for i in range(100000):
        for j in range(1, 10):
            v = {"x": 0, "y": 0, "z": i, "w": j}
            [globals()[ins[0]](ins, v) for ins in instructions[-1]]
            if v["z"] == 0:
                valid[13][i] = str(j)
    for k in range(13):
        old_z = valid[13 - k]
        new_z = valid[12 - k]
        for i in range(1000000):
            for j in range(1, 10):
                v = {"x": 0, "y": 0, "z": i, "w": j}
                [globals()[ins[0]](ins, v) for ins in instructions[12 - k]]
                if v["z"] in old_z:
                    new_z[i] = max(new_z.get(i, str(j) + old_z[v["z"]]), str(j) + old_z[v["z"]])
    return max(valid[0])


def second(inputs: str):
    instructions = [d.splitlines() for d in inputs.split("inp w\n")][1:]
    instructions = [[j.split(" ") for j in i] for i in instructions]
    valid = [{} for i in range(14)]
    for i in range(100000):
        for j in range(1, 10):
            v = {"x": 0, "y": 0, "z": i, "w": j}
            [globals()[ins[0]](ins, v) for ins in instructions[-1]]
            if v["z"] == 0:
                valid[13][i] = str(j)
    for k in range(13):
        old_z = valid[13 - k]
        new_z = valid[12 - k]
        for i in range(1000000):
            for j in range(1, 10):
                v = {"x": 0, "y": 0, "z": i, "w": j}
                [globals()[ins[0]](ins, v) for ins in instructions[12 - k]]
                if v["z"] in old_z:
                    new_z[i] = min(new_z.get(i, str(j) + old_z[v["z"]]), str(j) + old_z[v["z"]])
    return min(valid[0])


def add(instr, v):
    try:
        v[instr[1]] += v[instr[2]]
    except KeyError:
        v[instr[1]] += int(instr[2])


def mul(instr, v):
    try:
        v[instr[1]] = v[instr[1]] * v[instr[2]]
    except KeyError:
        v[instr[1]] = v[instr[1]] * int(instr[2])


def div(instr, v):
    try:
        v[instr[1]] = math.floor(v[instr[1]] / v[instr[2]])
    except KeyError:
        v[instr[1]] = math.floor(v[instr[1]] / int(instr[2]))


def mod(instr, v):
    try:
        v[instr[1]] = v[instr[1]] % v[instr[2]]
    except KeyError:
        v[instr[1]] = v[instr[1]] % int(instr[2])


def eql(instr, v):
    try:
        v[instr[1]] = 1 if v[instr[1]] == v[instr[2]] else 0
    except KeyError:
        v[instr[1]] = 1 if v[instr[1]] == int(instr[2]) else 0


def get_input():
    return """inp w
mul x 0
add x z
mod x 26
div z 1
add x 13
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 5
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 14
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 15
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 11
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 16
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -16
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 8
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -11
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 9
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -6
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 2
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 11
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 13
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 10
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 16
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -10
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -8
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 6
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -11
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 9
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 1
add x 12
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 11
mul y x
add z y
inp w
mul x 0
add x z
mod x 26
div z 26
add x -15
eql x w
eql x 0
mul y 0
add y 25
mul y x
add y 1
mul z y
mul y 0
add y w
add y 5
mul y x
add z y"""


if __name__ == '__main__':
    main()
