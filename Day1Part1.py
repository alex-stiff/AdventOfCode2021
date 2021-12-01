from helpers.input import read_input_int
import math

class Day1Part1():
    def __init__(self):
        self.input = read_input_int("input/day1.txt")


    def solve(self):
        previous = None
        increases = 0
        for i in self.input:
            if previous is None:
                previous = i
                continue

            if i > previous:
                increases += 1
            previous = i
        
        return increases


if __name__ == '__main__':
    d = Day1Part1()
    answer = d.solve()
    print(f"Answer is {answer}")
