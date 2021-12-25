from typing import List


def main():
    print("First test: ", first(get_test_input()))
    print("First real: ", first(get_input()))


def first(inputs: str):
    data = inputs.splitlines()
    i, ce, cs = 0, True, True
    while ce or cs:
        data, ce = move_east(data)
        data, cs = move_south(data)
        i += 1
    return i


def move_east(cucumbers: List[str]):
    c = []
    changed = False
    for r in cucumbers:
        edge = (r[0] == '.' and r[-1] == '>')
        changed = changed or r.find(">.") >= 0 or edge
        s = r.replace(">.", ".>")
        if edge:
            s = '>' + s[1:-1] + '.'
        c.append(s)
    return c, changed


def move_south(cucumbers: List[str]):
    c = []
    changed = False
    for i in range(len(cucumbers)):
        a = zip(cucumbers[i-1], cucumbers[i], cucumbers[(i+1)%len(cucumbers)])
        cc = []
        for b in a:
            if b[0] == 'v' and b[1] == '.':
                cc.append('v')
                changed = True
            elif b[1] == 'v' and b[2] == '.':
                cc.append('.')
                changed = True
            else:
                cc.append(b[1])
        c.append("".join(cc))
    return c, changed


def get_test_input():
    return """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""


def get_input():
    return """>vv...v..>.v>.>v...>>>>vv...v.>..>..>>v>v....v..>>.>v...v...>.>..v>.>>..>.>v.v...>v>v.>v..vv>>>..>....v.v.>.v.......v>....vv..>.>vv>v>>>.>.
>.>..>>........v....>...v.v.>.v>v.v...........>..>>vv...v.v.v>>...v>>v>...>v...>>v....v.>.>>.>vv..>...>...v.>.........>.vvv.v.>.>>>..>..>v.
.v.v>v.v.v.>.>>>v.>>.v.>v..>.v.vv.....>.>v.>>.>..>.v.vv>....>.v>.v.....>.vvv.>>v.>.>.v...v....>vv>.v...v.v...v>vvvv.>v>>>.v>v>...>.v..>....
>.v.>v>...vv.>...v.>..>.....>>..vvv..v.>>>...>v.v.v>.v..vv...v>.>.>vv......v....v>vvv>.vv.>..>>>...v..vvv..>v>>v>.v.v..>v.>vvv.>v.v....>.v>
...v.v>v......v>.v.v>>>.v>vvv..v>v...v.v.v>..>...>.>vvvvv..>vvvvv>.>>...v.v>>>..vvv....vv...>vv.v.v.v.v.v>.v..vvv>>..>>v.>..vv.>vv>..>vv>..
.>....v...>>..>>>>>>v.v.vvv>.>..>...v..>....>.v.>.vv.....>..>>v.vvv...>.>>v>v.>.>....>.v>.vvv..v>.>>....>vv....>>.v.>..>v>>...v...v.>..v.>v
.v..vvvv.v..v..>....v>..>v>.v.>...>v..>..>vv>>>...v..>vv..>v.v>>..v....v>.>.v>..>vv.>>.>..v>.>v.vv.>...vvv..>v.v>v>>v>vv.v..vv>.>>..>.>....
.>..>>.v>..v.vv>.v....>v>v.v>.>v.vvv>v.....v.>>...vv>v..v...>>>>..vvv>v.v.vvv>v....>>v..vv...vv....>>>.v.vv.vv..v>v.>>v.......>.v.>v>...v>v
vv..>>....vvv..v..>v..>>..v...>...>>v>>>..vv..v>>.vv..>.>.v>.>.v...>>v.>..>>v.v...>>vvv.v.>..>.v.v.>vv>....>..>v...vv......>v>....>.>.v>>..
>>>.v>.v>vv..vv>vvv>>....>>>v.v..>..v>v..>vv.v.>>..v>>vvvv.>..v>.v>.>..vvv....v..>....>v.v.>v..v>>>...v>...>...v..>v>.>v>...>.v.>v>>>>>v>>v
...v...>>.v..vvv.v..>v....v>vv.>......v>.v.vv.>vvv>..>.v>vv>...>>.>.v....>v.v..>.>.>>.>v>.>...>v>vv>..>vvv....v..>..>>v.v.v.>>..v....>.>.>v
.>.v>.v>vvvvv.>>>.....v.>>v...v..>.>.>>>.>.v>...>vv>....>..vvv>vv.v.>>....>>..vv>>v.>...v.v.>>v.>...>v>...>v.>vvv...>.>.>vv....>>>..>.v>..v
.........>>v.>.v.>....v..v>...>..vv.....vv>v>..v.v......>v..v>>.>..>.>..>...>>.v>.vv.>.>..v.>.>v>v.>v>.>>v.v>.>vv.>>v.v.....v.v.>>vv.v.v.vv
...>v>.>.>>.v>...>..>v.>>>.>>>>>v..>...v....>..>...>>..>vv....>.>>..>v....>v>>.v...v.>..v>v>.>.>v>>>v..v.......>...>....v..v>v.v.vv.vv.v...
v..>..v.v..v>...vvv.v.>.vvv.v>.....v.>>v>.>>>.v....>..v>....>.....>..v>..v>>.>.>>v..vv...vvvvv.>>...v..>.>>v.v..>vv......v>>>.>>.vv>...>v..
...>..v>..>..v>>vv..>.>.v>v..>>>.>..vv.>.v..v.vv.>.v.>>.v.>>v.v......v....v..v.v>.>v.v....>>>.v...v.>..v.v.v.>>v.v..v>>>v>vv>.....>v...vv>>
....>..v..>...v..>v...v.>.v.>.vv>.>>....>..>v>v.>....>>.>v>v...>>..>v.v>...>v.v.v..>>......v.v..v>vv.>>>v>v.v.vv..v.v.v.v..>....v.v>v>.v>v.
..>vv.v..>.v>..v..v>>.v.>vv...vv>.vvv.>>>.....v..>>>.v.v...v>>.vv..>..v.>>.v.......>>....>>.>>........>.>.>.v.>..v....>vv>v.>.>vv>v.>vvvv>.
>.>>...>.v.>...>...vv...>.>.v.>.>..v.vv.>>.>v>.v>...v.v>>.>v..>....v.>..v>..>>...v.v.>v...vv...>v>v.v........v.vv.>.v.>...v>>v>v..v>......v
.>.>.v.>..>>.>.v....v..>v.v>.>>.>>.>.>v..vv.v..............v.>v.>.v.>>.......>>>vvv>.>>v..>.v>>..v>.>..v>....vv.>vv.vv.v.>..>..v>>v.v..>..>
..>>.>.v>.....v.>v>.>vv>>..>...vv.>.>.>>v>.....>..>..>.vv>v..>..v>>.v..>vvv.>v>v>...>>v.>v>..>..>...>.>>>..>.v>.v.v.>..v....>v...>>v.vv..v.
>....>...>..>v>v.v...vv.v>v>.>..>>vv>...vv...>..vvv...vvv..>...v>>.>.>.vvvv.>v.>...>.v.>v>.>>..vv>.vv..v>vvv.>>..>.>...>.vvvvvvv..v..>...>.
>.vv>.>>.v......>.v..v.>..>.>.vv....v>v....>vv>>......>..>.>.>v.>v...>.v.>>v.>.>...>.....v.>>vvv....>..v..v>>...>.>>>....>>>>v.>v>.>>>..>>.
...vv>v.>.v>.vvv...v.>>.>..v.v.vv..>.v>>.>.v...>>v>.>>>.>>.v...v......>.>>.>..v...vv.>v>.v.v.>v>>..v>...v...>v..>v>>.v....v..v..vv..v>v>>>.
>vv...>..v...v.>v>>.v..vv>..>v>vvv....v>vvv......v>v..>vv..>.v.v.>v.v.v.v>..v.>.>....>..>...>....>.>....>v>v.>>v..vv.>.v>vvv...v.v..v.>v.v>
>vv.>......>..>>v.>...v...>..v.......>.>v>..>>.>v>...v.>v.>vv.>.v..>v..>v...>.v>>...vv>..vv..v.......>.>....v.>>vv.v..>.>......>.v.....vv.>
......vv.>v>v.vvvv.v>.v.>....v>>..v..>...v.>...v>>....>.>..v.>.>.>v.....>v>vv>..vv>v.....v.>>v.v.>.>..>..>...>v....v>>vvv..v.>>.v.>.v....vv
v...v...v>>>v.v.>v.>>..>...v..v...vv..v..v.v.>.v>v.>>v.v>..v.>v>v>......vvv>v>v>.>v.vv.>v...v>>>.vvv.vv>v..v..v.vv.v.vv.>.>...vvv.v..v...>.
>...>vvv>.>v>>v.vvv.........>>..v..>.>>.vvv>.v.....v.....>..v...v.>>>v>...>.v..v>v..v.>>.v.>.....vv>v...vvvv.>vv>>>..>>.v>..vv.v..v.>..>..>
>....v......v>..v....vv.>...v.>.>.v>v..>>...v.>.>..v.v.v..>v.>.v>.v>.>.v..v.>.v......v..vv>..>..v>v....>.vvv.v..>....v...>v....>vv.v.v>v..v
.v....v..v...........v>..v..>>>v.v...vvv...v..>.>.vv.>v...>.>.vvv.>...>>...vv.v>vv>>.......v>.v..>.v>vv.>v..>vv>.....>.v...v...v>>.>...>>>>
..v>>...>.>>vv..>vv...vv>.v>vv..v.v..>vvv.vvv>.v.v..v>v.v...v>.>..>.>.>vv.v..vv....v..>.>..v.>.>>>v>.>.>v>vv....vv..v>..v....v.v..v.vv>>...
.>..>.>.v..v>.>v>>v..v>>>...vvvv.>.>>>v.vvv>.v..v.v.>..v..vv.v...v.>....v>v.>.>v.>...v.v...vv>>....vvvv...v>.v.>>..>vvv>v>>..vv.>.vv>v.v..v
.vvvv.v.>.>.>v..v....vv.>...>.>v....vv..>...>.>..vv.>>.vv...v>.>.v.>..>.v>>>>..>..vv>>vv.>v>v.v.>>>v.v.vv.v..v..v..v..v.>v....>.v.vv.>..>vv
v.>v....v>.vv>....v.>>.v.>.>vv>v>....>.vv>.....>..>.v>vv.>v>...vvvv>.>.vv.....v>v.v>.>.....v...v.vv>.>v..>v..v>>.v..v.v>>..>>.vv.vv.....>>>
...v>..>v.>v>>.>v...>.vv>....>v.vv>>.v>>......>.v>.v..>>>.>>>....>.>..>>.>.>.>>>v.>>.....>v..vv....v>>.vv>v..>>v..v>.>..>vvvv>....>..>.....
vv>..v...>v..v..>.>..>>v>>>vvv..v>>v>v..v>vv....v>>.>v...>>>>v.>.vv>vvv>>.v.vv....v.v>.>v....v.....v.>.>....>.>v.vv..>vvv.v.>.>>v>v>.>>..v.
.>.....vv>>>....>v...>.>.v>.>vvv.vvvv.>......>>.v>.v.>>v.v..v.....vvv..>.>v>vv.>>>...v.>.vv>v..v...v....>vv>v.vv>>vv.v...>>v>.>.>v..>..>v..
....v..>........v>>.v..vv>.v>>.v...>...>.>>v.v.v.vvv...>>.v>>v>.>vvv..v..>v>v.v.vv..v>..vvvvv..vv>>.>>>...v.>.>.>>>>..v>..v.v.v>.v>.>...>>.
v.v..v...v..vv>...v...v>..>v>.>v.vv...>.v>.v..>>..>..>>>..v..v...v>>.vv>>>v..vv.v.v...vvv..>..v.v..>....v..>>v..vv.v.v>.v>>.>.>.>>>..v.vv..
...>v>>vvv..v.v...>v>..>>>>>...v>..vv.>..v..>>..v....>v.>v.>>.vvv>...>.v..v.>>...>.>..vv.>..v>..v..>.>v.>v..>v.v>vv>.v.>>>..v..........>.>.
v.>v.vvvv.>..v.vv.v........>vvv..>.v>...>v.>>v>>.>.>.......>v>v.>>...v....v..>..>..v.vv..v>.>......>v.v...>.vv.>>v...>.v..v.v>v>>vv.vv.>.vv
v.>..>>>.>.....>.>v..v.>.....>>v..v>>>v...vvv>..vv....v>.>.vv.>v....v>v...>..v..>..v>..>>.>>.v.v.>>.v>vvvv...>.>.....v>.>>.>v...v>..v>..>..
.....>.v..>>vvv>v..>>..>.v>>v.>>>>>.vv.>>>>..vv.>.>..>......>v.v.>>>v.....>>v>.>>v.v...v.>..v.>>.>>.vv..v....v.vv........>.>v..v...vv>>>.>>
>v.v.>.....v.>.v...v..v.v>v...>...>..v.>>..v..v>v>>.v....v..>.>>>...vv>>....v.>......v>.v>>..vvv..vv..vv>.>vv.v>vv....>.v.....v.>>.vv.vv..>
>..v.....vv>v..v.v.v.>>.v>.>>>.>..>vv...>vv.vv.v.vvv>..>.v>v.v>>.vvv>...>>...>..>.>.>v>v>v>.>>.v.v>v>..>.vv.vvvv..>..>...v.v>>>.v>...vv.v.v
>>..>.>.vvv>.>>v>...>vv>>..>vv.>....>>.v..>vv...v>.>..>.v>...vv>..vv>v.>.v.vvv.>v....v..>v.v>v..v.v.v.>>vv>v.vv..>>.v.v.>>>..>..v..v>......
>v..>vv>vv.>.v..v>...>.>....>..>.v.v...v>..v>v.v...>.>>.>..v....>>..vv.v.>v.>.vv>>.>.>.>...>.v.........vv..vvv...>>.>..>...>.>>v>..v.v.v.v.
.>>>.>v..>.....v...>..v..v>v>..v.....>.>v>>.v..>.>v....>.v..>>..v>....v>.vv..>>...........v..>.>...>v..vv.v>.v........v.>.v...>vv>.>>..v>>>
v.>....>....vv.>v.v>v...v.>>..>v.>...v....v.>>>v...vvv.>...>...>>v>...>>vvv..v..v.>v.>>>..>.v>vv>.>..v>.v.>v..>v.v.>v.>>.>v..v.v.v>vvv>>.>.
v.....>vv.vvv....>v....v>.v..>vvv>v>>....v...>.....vvvv>v.vv>.>v>vv.>.>.>.>v.>.v..>.>>v>>...vv.>.v.>.>..>..v>.>>>v>v.vvvv..>..v.>v>.>vv>..v
vvv.>>>..v.v.v.v..........v.>..>.vv.v.....v>....v.v.vv>.>.v>vv...v..>v>.v>...>v..>..vvv.>>.>vv>v>..vv.>v....v..>.>>>.v>>.v.>vv....vvv>.>..>
.vv.v...>..>.>.>v>v.vvv..v>>vvv.>.>.......>.>.>v.>..>>.>vv>v>.vv.v...>..v>.>>..v.v.v.>>.v>.v.v>>..>>.>...v>.v..>>.....vvv>.>v>v.>..>>.>v..v
>vv..>..vv..v...>>.>.>>>.>.v..>...>..>>>v.v.>.v.....>.>...v>v>..>>.>v>.v.v>..v>..v.>>>.v>>>v>v..v>.vvvv>v..>>v.v>..v..>.v..v.>v..v.v..>.v.>
>..v..v>v>v.vv.>.>>>.v>.....>.>>..>v>.v>.>..>v.>v.>>.>v...>.>>.>>.vv.v>..>v.......>>...>.vv....v...>>>>>.>.>.v...>>v>vv.v>.....v>v..v>...vv
>>v>..v.>.v>v...v>.vvv>v>..>>..>.v>>.>v...v...>.>v>>.vvv.>v..>>...v.vv>.....>vv...>v.v.>v..>>v..vvv.v>>..>.v.v.v>vvv.....>>>v>..v>...v>v.v>
v>.>>.>.v.v>..>v..v.>>>..>....v>..vvv>.....>>vv>v>....>.>...>>vv>>..>vvv>..v..>..v...v.>...vv.v.v.>..>>.v.>>v.......>>>..>..>........v....v
..v>.v..v>>>...v.>v....>>>.>...>.v.v.v>v..v...v>..>>>>>.>.v.v..>v...v.>.>>v>...vv....v>>>.>.vv.>.v....v..>>....>v.v.v..>.v...>.v>.>...>>.>v
....>v..v...v..v.....>....>vvv>>....v.vv.v.>.v...>>>..v...v.>>>.>vv..>..v>>v>v>..v>...>.>...v....v.v...>.>..>.v..>v>..>..>v....>vv.vv....>>
....v.>v>.v>...>>v>.>..>....v.v>v>.v..v>.v>vvv.v>.>v.vv>.......v>.>>>.v....vv.>....>>...v......>>.v>>vv>>>.>>>vv.v>.......v.>v.>.>....v.>..
....vv.........v>.v.>..v.>.v..v>vv..vv..v.v..v..>..v..>>.v..>v...>..v>.>...>.v....v...>.>....v..>...v>>.>v.>.vvv>..>..v.>>v.>vv.v>...>..>..
.>.>v.>..v>....>v..>...v..>...vv..>.>v..>..v.>v..>v.>.>v>vv..v>vvv.v>>>..>.>>v....v.v..>>....v..v.vvv...>>>v...........>..>>.>>>..vvv...>..
.vv..vv...>>vv.>v.vv..>.v...vvv....v...v>.v.>..>>.>v..v..v....>vv.>.v.>...v...v>.>..v>>>vvv...v......v.v.>...v.v>..v>vvv.>......v..>.......
>>>..>vv>>>v>.>>>....>>>..v>.v.>.v..v>v>>v.v....v.vv.>v>....>v>>..v.........>.v.>v.>...v>>>..>>v....v.v>v..>..>>v....v..v>..v.v..v.>.>..>v>
>>.>>v>vv>v.vvv.>>>>v>...>..>>>>.v>v>..v.>>.>v..>.>v..v.>>.>>v.>..>vv.>...v.v>>v>.vv>..v...>>..v...v.v...>v..v.v.>>....v..>.>.v.>>.>.v..v.v
v.vv.>v.v>...vv.v...>.v>>..v....>.v....>...vv.>v>>..>.v.v.v.>.>>>.>.v.v.>.v.>.....v>..>v.v....>>....v>.>.v.v..>..>v>...v...>.>>...>...vv.v>
...>v.......v.>.vv>>.>>...vv.....v...v.vv...>v.v>.>.>.>>...>v....v.>>....>v.>>.v.v>v.>...v.vv.v.>.>>>.vv.vv>v>...>...>.v.v>>v>.>vvvv>vv.>v.
v..v.>v...v>>.>v....v.......vvv...v....>v..vv>v>v..>.vvvv..v.>>.vv.v.v.v>>v..>v.vv..>v.>.v>.>.>vv>.v>......>..vv.>>>.v.v.>..>v..v.>v>>>.v>>
..>>v.>...>v>.>>.>.v....>>v.v.>vv..>>....v>>.vvv.v>.....>v.....v>.>..>v.v.......v..v.>>>>.v>>v.>v>...v....v..v.v...>.>v...vvv..v.>..vv.v...
>vv>.v.vv..v>v.v...v......>>.>v.v.v.v.......v...v.>.vvvv.......>....>.v>..v.....>.....>>>vv...>v>.v...vv.v>>>....>v>..>v..>v.v..>v.>.>.>>..
.>....v..>>..vv...>....vv.>>v>>>...>>v>..>.v...v>.v.vvv.v...v..v..v.vvv...>v.v....v.>vv.v>>...v>>v.>>v..v.v>.v>.......>..>v>v.vv>.....>>.vv
v.vv>.>v...v>....v.>.v.>...>>v.>.>..>v.v.vvv....v>>vv.....>v..v>..vvvv.>.v..vv>>...>>>.>.>>...>...v...>v>vvv.v>>....v.v.v.v...v>v.....>v>..
.v...v>.>v..>v.v..v.v..>>.>..v..v>.v..>..v>.>v.>..>v.....v.>..>.v>vvvv.>..v..v>.v>.vv.v.v>.>.v.....v..v.>>>>.v.vv.vv....v>.>v...v..v>.vv>.>
..>v..>v>..vv>..vv>v>v..v.>>vv...v>v...>v>v.>.>vv..>.>....v.v.v>v..v>..>>vvv..>.>>v>...>....>v>vv......v..v>>..vvv..>..>v.vv>v.v.........>v
..v..v>>.v....>>.>vv>>v.>..>.>...vv..>v>.>....v.....v>>.>...>v>>>v>v.vv..v>vvv>.vv...v...>...>>.v...>v.....v>vv...v......>>>v.>>.>.>.v>.v.>
v>>..v>...v>.>v...vv.>.v>..v.v>>.vv..v........v.>..v.>>>v>v...>.vvv.>>v.>.vv>>.>.v..>..v.v>.v..v...>..v>.v..>..v>.....>.vv>v..>>.>>.v....v.
>vv.v>>v.vvv..vvvv>>v..v...>>.>>..>..vv>...>v....>v>v.....>.....>>....>...>..vv.v....>v>>>>v......>...vv>>.v..>.v.>.>.v..>.>......>v>vv.v..
......>.>..>vv>.vv>>...vvvv....v.vv...v>>v>....>v.>...v.vv.>..v>.v>>vv.>....>v.>.v.vv.v>.vv>...v.>v>.>>..v>>v..>v.v...>....v.v....v>v.>.v.v
>v>v.>vv....>.v>.v..>.>.>..>.vv....>.....>v>>..>>.>.>.>.>v.>...v>v..v>vvvv.>>v...>vv>>..v..v.>>.v.v>vv.>...........>.>.....>>.v..>.>...v..>
v>v>>...>v..vv.........>v...v..v>.>..>>>>.v>..>v>>...>v..>>.....>.>.>>>>..vv.>vv....v>..>..>..vv>....vv.>>>...>.v..v>v......v>v>.v.v.v>.v.>
>v..v>.v.....>>.v>>...v..vv>.>>>..v..v.>>..>..v....>v...>vvvv>.vv......v.>vv>>..v...v.>v>..vv.>.vv......>..>>>.....>......vv.>>>>>vv....>vv
.>...v.v>.....v.>...>v>v..vv>>>>.>>>>v..vv.vvv.>>..>.>.v.>>.>v>>.>.>>v.v..v....v...v....v>>..v>..>.v.>v>vv>.>.>.>..>v>>.>..v...>.v>.....v.>
vv..>..v...>>>..>v.>>..vv>vv.v.v>.v....>>v..>.>>v>>v.>v.v>.v>...>..v>...v>v>....>.>>..v>vv..>>.v.v.v>v>>.>..>v>..>.>>v>>....v>..>.....>>..v
v.>>>.v..v>.>...v....v...>...>v.v...>..>..vv>.v..v>..v>.>v...v>>.>..v..v.v>.v.vv..>v..>..>.>..vv....v>v.>vv>.v.>.vv...>v.>v>vv.>v..v.v..v..
v.>v..>..v...v..v....v>.vv>v.>>.v.>v....>>.v.>v>>.......>>>..v..>...>v.v.>>>v........v....v.vv.vv>>..v>..v.v..v....v>.>v.>>...v>>..v...v...
..v>>..>>......v..>>.v.vvv>....>>vvvvv>vvvvv>v..>v>.v>vvvv..>....v>v>.v.>v>.>.>.>...>.>v.>.>..>.v>>v.vv>...v..>>v>>.>v>v>.v....vv..vv..>.>v
..v.>v.>v.v>>.>v.v>>.>.....v>v.v>vv>.vv>..>v.>...vv..>>vv.vv.>.v.>>>....>.>>>.>v>..>.v.v....>>>..v.>>.>..>>>.>>>>>....v.vvv.>.v.v.v>v>.>.>.
>>vv..>...>.>.vv..>>.>.vv....>..>.>vv..v.>.v>..v..>....>v......>..>.>vv..>.v.>>>..v.>v>>v...vv..v>.v...>>..v>..>.v.v.>v..>>>...v..>>.v....v
..v.v..v>v.>.>..>v.v>>..>v.>.>>.>>>.v..v.>....v...v.>...>>v>.v....>.v.v>v>.>>>.>v.vv..vv...v>>.v...>vvv.>.vv.v....>>v.>>....v..>...v..v>..>
.>v.vv..vv>>v>v>......>.....>>....vv>v...>......>..>....v>>v....v...vvvv.v....>v.>>..v.>>v....v.......vvv..v.>>>v....v.v...>.....v..v.....>
>....vv.....>.v...v..v.v.>>>>.vvv>.vv>.>...v.v>..>>.vvv>v>.v..v.v..v>....vv.v>....>.....>>.vv.vv.v.v.>..>.v..v>>...>..>.>..v.>v...>.>......
.v.v>v>v>v>.>.>.vvv>.v..v>v>.v>....>vvvv.v>v...>>..v.>>.vv..v>>...v.v...>...>vv..>...>>>v.v...>>.......v.>..v>.v..........>>.>.v.>.>..v>.>v
..>>>>>.v.v......v...>..>>.>>..v...>...>>.....>vv...>>.>>.>v..v.vv..v..>>>..v>.....vvv..>>...>v.vv>>>...>vvv.>v>.v.>>..>>.>>v>>..>..v.v..v>
v..>...v....>>v....v.v>..v...v.v.v....vv..>..v...>vv>>>v>>vv>>v..vvv..>>>v.v.v.>>...>v..vv>v.v..v.>v.....v.>...>.>.v>v>.>..v>>>.v.v>.v.>v.>
>>.>vvv..>..v>v..>>..>.v.v..>.>v>.v...vv..vvv.v..vvv>..v.v.>....v..>.>..>...v.....v>.>...v.vvv...>...>>.>vvvv>>vvv.vvv....vvvv>>v....>>v.v.
v>vv>.v....>.>.>>>..>..>.>v>..>...vv>>>.>..v>v.v.>.v....v.>...>..vv.>.>.v.v>.v..>>>..v>v>>.v..v.....>v..vv>>.>.>v>..vvvv>.>.v>.v..v..v>>>v.
v.vv>>v>..v...>..>.vv>.v..vv......v.>>>v>v.>..vvv.>.v>>v..v.>...>.>....>...>v..vv.v..>.>vvv.v.v...>v.vvvvv...>>.vv.v>v.vvv..vvv.>.>..>>>.v>
.>>>>v.>>>.>vv>v>.....>>>v>v.>v.vv...vvv>vv>.>.v.v>v...v>.>.v>v>.v>>vv>.v.>...>vv.vvv>v>.>v>v...>.>vv..vv>.vv...>..v....v.>v.>v>.....>..v.>
v....>.>..>.>....>.>.vv....>v.v......vvv.v>vvv>..v.v>>.>vv>v>>..>>v>v>vvvvv.>>>>.v.>....v>v>..v.>.vv..>>.v>vv.....>>v..vv.v..v>.v..vv>.....
.>v..v>>vvv.v.....>.v.>.>.v.>v>...v.v..>>....>vv....v.v>>>v.>...>....v.v>>...v>.>>...>....vv.vv.v>>.>.....>vv.v.v.>>.>>v...>>>.vvv...>v....
v>.>.v.....v..>.v.v..v...v.v>.vvv...vv.>.v.>.v>>>.v>.........>>>..>..v..v.vv>>.>...>>.v...v..>..>>vv>.>vv..>>vv>.v.>.>..>vvvvvv.>>....v.>v.
...>>.v>.>vv>..>v.>..v.....v>.>.>>....v>v...v.vvv.vv...>.>..>v..v>.>.>v...v..v.>v.v>vv..>.vv>...v>.>...vv>>....v>v...vv.>>..>>.>vv>.>..v.vv
.v>v>.vvv.vv.>.v.v....v>v>....>>v..v......vvvv.>>....v>.....>vv.>..>v.v..vv.>>.vv>.v....v.........>>.vv..v.>.v....>.v.v..v>.v.>v.v....vv..v
vv.v............>.vvv.>.....>>.v..v..v>>v.>>v..>...vv>v.>.>.>vvv>..>>v>v.v>.>.>v...>v>v>.>>v.....v.>.>..>>>v>>vvvv>..>...>vvvv....v..>>v.>.
.v....>v.v.v.>.v>..>v.>.>.v.>>.>v..>.>>.>>v>>>vv>v>.>>.>.v.>..v>>vv>>v.>>>>>.>.>..>>...v>...>v..>.v>.v>vvv>.v....>v>>v...v>...>.>..>>.vvv.v
v>.....v>.>.....v...vvv...v.v.>.>..>..vv.>>.v>>>v>...>.vv>v.....>.>.>.v..v.>....vv.>.>......vv>v.v.v.vv>vv..>v>>>..>.>>..>>vv>.>>>v..v.>..>
vv..>.>.>..>.vvvv....v>...vv.v.v>vv......>>..v...v.....>>>>..v>v..v.v>..vv..v....vv..>>>..>>....>vvvv>.>.vvv>.>.>>>v.v>.vv>vv.....>.v....>.
.>>>.......v>....>.v>.>v...>>>>v.v>>.vvv.v>.vvvv>>..>.v..v>.v.>>vv>.....>...>>v>.v.vvvv.>.........>...>>>v...>vv.v.v>>..>..v.>.....>v>v>.>.
>.v...>......>..v.v.vv...v>.v.>v..>>>v>.v...>v.vvv>...vv>v.v.v.......>>...v...vvv>..vv>>v>...>.....v....v>.......v.vv...vvv>>>>vv>>.>......
.>>.v.>v.v.>...>.v..>>..v....>>vv>v...>..v>>vv..v..>>>v..vv>.vv...>.>....>>>.v..>.>.>.v>v....vv.>>>.>>v>>.>vv.>v>vv...vvvvv.>>.....>v...v..
v.v.v.vvv..>...>>v.>>..>v>>....>.>>......v.>v...>.v>.....vv.v.vv>>.v.>>...>.v.v.v..>>.vvv>v..v.v....>.v.v>v>>.v>>v.>.v.v>>>>.>..>>.>.v>.>>>
..>.v>..v..vv>v..>vv.>>.v.v>..v.>v..v.>.v>..>vv...v....>>v.v..>.....v>v...>.v...>v..vv.v...>.>.>v..vvv.>..vv....vvvvvv.>.vvv.>.>..>......vv
.v>.>.vv..v...vvv.>.>.>>>.v>....>...v>.....v.>.>>v.>..v.>.vvv.......v.v.v.>..>.vv>....v.>.v......vvv.v..>....>v.....vv>...>v.v.vv..v>>v..v.
.v.v.v..>>>.....vvv..>.>.....v>v>..>>>......v.>>v.>.vv>..>..v>v.....>>.vvv.>v>.>>.>>v>vv.vvv...v.>.....vv...>v.v.vvv..>.v>.>>..v>v>vvv...vv
.vv>>..vv.v..v...vv.>>....vvv.v>...vv.vvv..>...v.v.v>>.>.>.v..>>...>v....v>>.v.>vvv.>.v.>>.v.>v>>.v..v..v....v.>.v..vv.v>>.....vvv.v>.vv.>.
vv.v.>v...v>...........>.v>.>vvvv.>..>>>.....>>.v.v..>v>...v.>>.>>>.v.vv.v>vv>v>.>>v>v....v..v>..v>vv..>v...v..>..>>>>>.>.....vv>.>>>>...v.
.v.v..v>.vv..>>...v..>..>..v>>.>>vv>v....>vvv.>>.vv.vv>vv>v.vv>.>v..>.>.......>v....v>...>..v....v.vv>>....v>.v.v.v>..>v>.>.......v>.>>>>>.
vv....v.>.v>v>...v>.v.v>..v.v..>..>...>>.>.>...>....>....vv>v>>...>v.v...vv>v.v.v......>.v.vv..v>..>v...v.vv.>>>>...v.v.>.>.....>....>v>...
...>vv..>>vv.v>>....vv..vv..v>>...>.v>>>.v......v.v.>.v.vv....vv.v....vvv>>.v..>>vvvv...>.v.>>.>.>.vvv.v>.....v..>.vv.>..>..v>v>v..>..>>v.v
.vvv.>.vvv>.>v..v>..>v.v.>.>...>>.>>>.>.vv>>.>.>>>vv>..>>.>>.>.....>..vvv.>.>v.>..v..>v..v>v.v.>>.>v.v..vv>v..>.vv>v...v>>..vv>v.>v..v>v>>>
v>......v>v>>....vv...v>>v>..>>>>....v..>>...v..>v..>>.v>v.v....>>>.v..vv......v..v>..>.v.v>>>v.v>....v.v>.>..v>>>..>.v>>.v.v.>v>.v..v.v...
vvvv>>.>..>v.vvv..v.v>>..>..>v>>>..>....>.v>..vv...v.>.>v.vv.>>v>v>v.vvv..>.>v..>>>>.>....v>..v.>>..vvvvv.v>.>.>>.>v...v..>v>>vvv.v...>>>..
v.>..>.v>..v.>>.vv.v..>v.vv..>v.>...vvvv.v.vv..>.vv>..>v>..v>.....>....v>...v.v..>.v...>>v..>v.....v.>>vv>....>..v...>>>.>v.>.>vvv..>>.v.vv
..>.v.........>..>.......>.v.>>>>v.v.vvvv>..>v..v.>v>>v..v..>..v.v>>...vvvv.v...>.>...>>>>>>...v>.>vv>.>v>v>.v.v..v>.>.>v.v>.v>.......>.>..
..v.>>..>v..vv..v>>v....>>>....>.>>.>.>>v>>...>>>vvv>>v>..>..v....v..v..>v>...v.>>>vv.v.v>.>.v.v>>>..>.>.>v>v>v.>.vvv.v.>>>>>...>>v..vvv>>v
v.>.>>.vv.>.>...>v.>>v>...v..>v....v.>.>..vv..>..v>..v.v...v.v>.>>v>.vv.>..vv>...>v.>.v..v.>.v.vv>v>...v....>.>v..>.v..v>>v>.>...>...v.>.v.
.>.>....>>.v>.v..v....v>.>>>>.v...v..v...v.>..v......>>.>..vv>..v...v.v...>vv.>>..>....>>>.>v>vv>..>vv>.v>>.>..>.>vv.v...>.>...>v.>vv>vv.>>
.>...>.>v>..>vv....>.vv.>..v.v.vv>v..>vv..v>..>....vv>vv.v>>.v>>.vv>.>>v..>...v>....v>vv..>..v.v.v..v>.v..vv.v.v.>.>....v>v..>...>.>vv..vv>
>.v>...>>.>.v..>>v>.>...>.vv>.vv.>..vvv>.>vvv..>..>v.....v.>>vv...>v...v...v..v.v..v>>v>>>>.>v..vv......>..>.v.....v.>>>.>.>.vv>.>.>v.v.v>.
v...>.v.>v>.v.>....>....v.v>..>>v..>..>>>>..>..vv...>.v.>>>>>.>>v>>....v...>.....v..v>.....>..>....v...v.v..v>v.>....vv..v......v>>v...>..v
....v.v.>.v.v>.>>..>>.v..v>v......>...v..v.>>....>......v>..>v>>.>vv>..>v>vv>v..vv.v.>>.vvv..vvv>..vvv..>v>vv.>>.>v.v.>.>..v.>v...........>
vv......v.>.>v.>vv>>...>v.>..>v>v>>v.vvv>...>>..>.>..>>v.vv.>>>>>.v...vv..v.vvvv.>..>>v>.>>vvvvvv.v.v>.v.vv...>v>..>..v>v>v...>>.v>.v.v>..v
....v..>.>v.>v.......v>v....v....>v>.>.>v.v.v>..>.>..v.v>>.vvv........>..>.v..>.>>v.>...>>.>>......>>.>...>.>..v..>....>>.vv>.v.........v.v
....>>.v..>v>...>..>.>...v>....>>.vvv..>..v>.......>...v>v>>.v>.>...>.v.v.>...>>......v...>..v....v>>v......vvvv...vv.>>>vvv..>v>v.v.v.vv..
...v....>v..>.v.vv.>.v.>..>.>...v..>vv>..>>v>>.>.>..v.v.v..>vv.>vv.v..v...v>v>>.v..>.v>..>v.>.>..>vv.>v...>>.>...v.>.v.>>..>.>v.v>.>.vvvv.v
.v>v.>>....>>.>.>.v>..>...>.v...v..>.v..v....v.vv>>>>.vv.v..>....>..>v.>..v>>>....vv>.v.>...>..vv>.v.vv.>>.>...v>>v>.v.vv.....>.vv>.>..>...
..>vv.>..>.v..>..>...vvvvv..v.v>..>vvv..v.v>..v..v.>..>..>..>.>.>..v......v>>>>v.>>.v>...v..>>vvv..>>>>..>>.vv..>.>>..>vv>>..>.>vv.>.v.v.>v"""


if __name__ == '__main__':
    main()
