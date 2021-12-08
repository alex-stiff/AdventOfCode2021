from helpers.input import read_input
import math

class Day1Part1():
    def __init__(self):
        self.input = read_input("input/day2.txt")
        self.horizontal = 0
        self.depth = 0


    def solve(self):
        for instruction in self.input:
            direction, magnitude = instruction.split()
            if direction == "forward":
                self.horizontal += int(magnitude)
            elif direction == "down":
                self.depth += int(magnitude)
            elif direction == "up":
                self.depth -= int(magnitude)
            
        return self.depth * self.horizontal


if __name__ == '__main__':
    d = Day1Part1()
    answer = d.solve()
    print(f"Answer is {answer}")
