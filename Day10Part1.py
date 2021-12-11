from helpers.input import read_input
from helpers.colours import colour
import math

class Day10Part1():
    def __init__(self, filename):
        self.input = read_input(filename)
        print(self.input)

    def explain_line(self, line):
        pairs = {
            '>': '<',
            ')': '(',
            '}': '{',
            ']': '['
        }

        line_char = [c for c in line]
        parsed = []
        for c in line_char:
            if c not in pairs:
                parsed.append(c)
            else:
                if pairs[c] != parsed.pop():
                    return "Invalid", c

        if len(parsed) > 0:
            return "Incomplete", None

        return "OK", None

    def solve(self):
        total = 0
        scoring = {
            '>': 25137,
            ')': 3,
            '}': 1197,
            ']': 57
        }

        for line in self.input:
            status, incorrect_character = self.explain_line(line)
            if incorrect_character:
                total += scoring[incorrect_character]
            
        
        return total


if __name__ == '__main__':
    d = Day10Part1("input/day10_test.txt")
    assert d.solve() == 26397

    d2 = Day10Part1("input/day10.txt")
    answer = d2.solve()
    print(f"Answer is {answer}")
