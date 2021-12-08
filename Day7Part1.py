from helpers.input import read_input
import collections

class Day7Part1():
    def __init__(self):
        self.input = [int(k) for k in read_input("input/day7_test.txt")[0].split(',')]
        print(self.input)
        self.numbers = collections.Counter(self.input)
        print(self.numbers)


    def solve(self):
        min_distance = None
        for x in range(min(self.input), max(self.input)+1):
            distance = 0
            for k, v in self.numbers.items():
                distance += abs(x - k) * v
            if min_distance is None or distance < min_distance:
                min_distance = distance
            
        return min_distance

if __name__ == '__main__':
    d = Day7Part1()
    answer = d.solve()
    print(f"Answer is {answer}")
