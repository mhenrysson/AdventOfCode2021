class FourteenthAdvent:
    @staticmethod
    def main():
        print("First test: ", FourteenthAdvent.first(FourteenthAdvent.get_test_input()))
        print("First real: ", FourteenthAdvent.first(FourteenthAdvent.get_input()))
        print("Second test: ", FourteenthAdvent.second(FourteenthAdvent.get_test_input()))
        print("Second real: ", FourteenthAdvent.second(FourteenthAdvent.get_input()))

    @staticmethod
    def first(inputs: str):
        template, insertions = inputs.split("\n\n")
        insertions = [a.split(" -> ") for a in insertions.splitlines()]
        insertions = {a[0]: a[1] for a in insertions}
        for x in range(10):
            new_template = ""
            for n in range(len(template) - 1):
                new_template += template[n]
                if f"{template[n]}{template[n+1]}" in insertions:
                    new_template += insertions[f"{template[n]}{template[n+1]}"]
            template = new_template + template[-1]
        letters = set("".join([a for a in template]))
        count = [template.count(l) for l in letters]
        count.sort()
        return count[-1] - count[0]

    @staticmethod
    def second(inputs: str):
        template, insertions = inputs.split("\n\n")
        insertions = [a.split(" -> ") for a in insertions.splitlines()]
        insertions = {a[0]: a[1] for a in insertions}
        result = list(zip(template[:-1], template[1:]))
        results = {"".join(r): result.count(r) for r in set(result)}
        for x in range(40):
            new_result = {}
            for r in results:
                if r in insertions:
                    new_result[f"{r[0]}{insertions[r]}"] = new_result.get(f"{r[0]}{insertions[r]}", 0) + results[r]
                    new_result[f"{insertions[r]}{r[1]}"] = new_result.get(f"{insertions[r]}{r[1]}", 0) + results[r]
                else:
                    new_result[r] = results[r]
            results = new_result
        letters = set("".join([a for a in results]))
        count = [sum([results[k] for k in results if l in k]) for l in letters]
        count.sort()
        return count[-1] - count[0]

    @staticmethod
    def get_test_input():
        return """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

    @staticmethod
    def get_input():
        return """VCOPVNKPFOOVPVSBKCOF

NO -> K
PO -> B
HS -> B
FP -> V
KN -> S
HV -> S
KC -> S
CS -> B
KB -> V
OB -> V
HN -> S
OK -> N
PC -> H
OO -> P
HF -> S
CB -> C
SB -> V
FN -> B
PH -> K
KH -> P
NB -> F
KF -> P
FK -> N
FB -> P
FO -> H
CV -> V
CN -> P
BN -> N
SC -> N
PB -> K
VS -> N
BP -> P
CK -> O
PS -> N
PF -> H
HB -> S
VN -> V
OS -> V
OC -> O
BB -> F
SK -> S
NF -> F
FS -> S
SN -> N
FC -> S
BH -> N
HP -> C
VK -> F
CC -> N
SV -> H
SO -> F
HH -> C
PK -> P
NV -> B
KS -> H
NP -> H
VO -> C
BK -> V
VV -> P
HK -> B
CF -> B
BF -> O
OV -> B
OH -> C
PP -> S
SP -> S
CH -> B
OF -> F
NK -> F
FV -> F
KP -> O
OP -> O
SS -> P
CP -> H
BO -> O
KK -> F
HC -> N
KO -> V
CO -> F
NC -> P
ON -> P
KV -> C
BV -> K
HO -> F
PV -> H
VC -> O
NH -> B
PN -> H
VP -> O
NS -> N
NN -> S
BS -> H
SH -> P
VB -> V
VH -> O
FH -> K
FF -> H
SF -> N
BC -> H
VF -> P"""


if __name__ == '__main__':
    FourteenthAdvent.main()
