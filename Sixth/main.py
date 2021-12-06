class SixthAdvent:

    @staticmethod
    def main():
        SixthAdvent.first()
        SixthAdvent.second()

    @staticmethod
    def first():
        inputs = list(map(int, SixthAdvent.get_input().split(",")))
        print(SixthAdvent.count_fish(80, inputs))

    @staticmethod
    def second():
        inputs = list(map(int, SixthAdvent.get_input().split(",")))
        print(SixthAdvent.count_fish(256, inputs))

    @staticmethod
    def count_fish(days, inputs):
        fishes = [0] * 9
        for i in inputs:
            fishes[i] += 1
        for _ in range(days):
            fishes = fishes[1:9] + [fishes[0]]
            fishes[6] += fishes[8]
        return sum(fishes)

    @staticmethod
    def get_test_input():
        return "3,4,3,1,2"

    @staticmethod
    def get_input():
        return "5,1,1,4,1,1,4,1,1,1,1,1,1,1,1,1,1,1,4,2,1,1,1,3,5,1,1,1,5,4,1,1,1,2,2,1,1,1,2,1,1,1,2,5,2,1,2,2,3,1,1,1,1,1,1,1,1,5,1,1,4,1,1,1,5,4,1,1,3,3,2,1,1,1,5,1,1,4,1,1,5,1,1,5,1,2,3,1,5,1,3,2,1,3,1,1,4,1,1,1,1,2,1,2,1,1,2,1,1,1,4,4,1,5,1,1,3,5,1,1,5,1,4,1,1,1,1,1,1,1,1,1,2,2,3,1,1,1,1,1,2,1,1,1,1,1,1,2,1,1,1,5,1,1,1,1,4,1,1,1,1,4,1,1,1,1,3,1,2,1,2,1,3,1,3,4,1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,4,1,1,2,2,1,2,4,1,1,3,1,1,1,5,1,3,1,1,1,5,5,1,1,1,1,2,3,4,1,1,1,1,1,1,1,1,1,1,1,1,5,1,4,3,1,1,1,2,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,3,3,1,2,2,1,4,1,5,1,5,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,5,1,1,1,4,3,1,1,4"


if __name__ == '__main__':
    SixthAdvent.main()
