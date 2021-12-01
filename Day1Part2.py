from helpers.input import read_input_int
import math

class Day1Part1():
    def __init__(self):
        self.input = read_input_int("input/day1.txt")

    def calc_sliding_window(self, i):
        return self.input[i-1] + self.input[i] + self.input[i+1]

    def solve(self):
        previous = None
        increases = 0
        for i in range(1, len(self.input) - 1):
            if previous is None:
                previous = self.calc_sliding_window(i)
                continue

            new_value = self.calc_sliding_window(i)
            if new_value > previous:
                increases += 1
            previous = new_value
        
        return increases


if __name__ == '__main__':
    d = Day1Part1()
    answer = d.solve()
    print(f"Answer is {answer}")
