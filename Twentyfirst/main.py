import math


def main():
    print("First test: ", first(get_test_input()))
    print("First real: ", first(get_input()))
    print("Second test: ", second(get_test_input()))
    print("Second real: ", second(get_input()))


def first(inputs):
    roll_sums = generate_dierolls()
    players = [player_sums(inputs[i], roll_sums[i]) for i in range(2)]
    krolls = [math.floor(1000 / players[i][-1]) for i in range(2)]
    for i in range(2):
        m = [n for n in players[i] if n < 1000 - krolls[i] * players[i][-1]]
        krolls[i] = krolls[i] * 50 + len(m) + 1
    winner = 1 if krolls[1] < krolls[0] else 0
    rolls = krolls[winner] * 2 - (winner + 1) % 2
    loser_score = math.floor((krolls[winner] - 1 - (winner + 1) % 2) / 50) * players[(winner + 1) % 2][-1] + \
                  players[(winner + 1) % 2][
                      (krolls[winner] - 1 - (winner + 1) % 2) % 50]
    return rolls * 3 * loser_score


def second(inputs):
    positions = {(inputs[0], 0, inputs[1], 0, 0): 1}
    wins = [0, 0]
    scores = [set() for _ in range(21)]
    scores[0].add((inputs[0], 0, inputs[1], 0, 0))
    while positions:
        key = next(p for p in scores if p).pop()
        p1, s1, p2, s2, player = key
        count = positions[key]
        p = [p1, p2]
        s = [s1, s2]
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    pp = (p[player] + i + j + k - 1) % 10 + 1
                    if s[player] + pp >= 21:
                        wins[player] += count
                    elif player == 0:
                        positions[(pp, s[0] + pp, p[1], s[1], (player + 1) % 2)] = positions.get(
                            (pp, s[0] + pp, p[1], s[1], (player + 1) % 2), 0) + count
                        scores[min(s[0] + pp, s[1])].add((pp, s[0] + pp, p[1], s[1], (player + 1) % 2))
                    else:
                        positions[(p[0], s[0], pp, s[1] + pp, (player + 1) % 2)] = positions.get(
                            (p[0], s[0], pp, s[1] + pp, (player + 1) % 2), 0) + count
                        scores[min(s[1] + pp, s[0])].add((p[0], s[0], pp, s[1] + pp, (player + 1) % 2))
        positions.pop(key)
    return max(wins)


def generate_dierolls():
    rolls = [[1, 2, 3, 4, 5, 6]]
    n = 7
    while n != 1:
        r = [(n + i - 1) % 100 + 1 for i in range(6)]
        rolls.append(r)
        n = (r[-1]) % 100 + 1
    sums = [[sum(r[0:3]) for r in rolls], [sum(r[3:7]) for r in rolls]]
    return sums


def player_sums(start, sums):
    ps = [start]
    for s in sums:
        a = (ps[-1] + s - 1) % 10 + 1
        ps.append(a)
    ps = ps[1:]
    for i in range(1, len(ps)):
        ps[i] += ps[i - 1]
    return ps


def get_test_input():
    return [4, 8]


def get_input():
    return [9, 10]


if __name__ == '__main__':
    main()
