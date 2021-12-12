class TwelfthAdvent:
    @staticmethod
    def main():
        print("First test: ", TwelfthAdvent.first(TwelfthAdvent.get_test_input()))
        print("First real: ", TwelfthAdvent.first(TwelfthAdvent.get_input()))
        print("Second test: ", TwelfthAdvent.second(TwelfthAdvent.get_test_input()))
        print("Second real: ", TwelfthAdvent.second(TwelfthAdvent.get_input()))

    @staticmethod
    def first(inputs: str):
        data = [i.split("-") for i in inputs.splitlines()]
        routes = [["start"]]
        going = True
        while going:
            going = False
            r2 = []
            for route in routes:
                if not route[-1] == "end":
                    for d in data:
                        if d[0] == route[-1] and not (d[1] == d[1].lower() and d[1] in route):
                            r2.append(route + [d[1]])
                            going = True
                        if d[1] == route[-1] and not (d[0] == d[0].lower() and d[0] in route):
                            r2.append(route + [d[0]])
                            going = True
                else:
                    r2.append(route)
            routes = r2
        return len([r for r in routes if r[-1] == "end"])

    @staticmethod
    def second(inputs: str):
        data = [i.split("-") for i in inputs.splitlines()]
        routes = [["start"]]
        going = True
        while going:
            going = False
            r2 = []
            for route in routes:
                small_cap = any([route.count(r) > 1 for r in route if r.lower() == r])
                if not route[-1] == "end":
                    for d in data:
                        if not small_cap:
                            going = True
                            if route[-1] == d[0] and d[1] != "start":
                                r2.append(route + [d[1]])
                            if route[-1] == d[1] and d[0] != "start":
                                r2.append(route + [d[0]])
                        else:
                            if d[0] == route[-1] and not (d[1] == d[1].lower() and d[1] in route):
                                r2.append(route + [d[1]])
                                going = True
                            if d[1] == route[-1] and not (d[0] == d[0].lower() and d[0] in route):
                                r2.append(route + [d[0]])
                                going = True
                else:
                    r2.append(route)
            routes = r2
        return len([r for r in routes if r[-1] == "end"])

    @staticmethod
    def get_test_input():
        return """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

    @staticmethod
    def get_input():
        return """re-js
qx-CG
start-js
start-bj
qx-ak
js-bj
ak-re
CG-ak
js-CG
bj-re
ak-lg
lg-CG
qx-re
WP-ak
WP-end
re-lg
end-ak
WP-re
bj-CG
qx-start
bj-WP
JG-lg
end-lg
lg-iw"""


if __name__ == '__main__':
    TwelfthAdvent.main()
