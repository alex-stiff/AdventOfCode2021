from helpers.input import read_input
import math

class Day10Part1():
    def __init__(self, filename):
        self.input = read_input(filename)

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
            return "Incomplete", parsed

        return "OK", None

    def get_finishing(self, line):
        pairs = {
            '<': '>',
            '(': ')',
            '{': '}',
            '[': ']'
        }

        parsed = []
        
        for x in line[::-1]:
            parsed.append(pairs[x])

        return parsed


    def solve(self):

        pt2_scoring = {
            '>': 4,
            ')': 1,
            '}': 3,
            ']': 2
        }

        pt2_totals = []

        for line in self.input:
            status, data = self.explain_line(line)
            if status == "Incomplete":
                to_finish = self.get_finishing(data)
                pt2 = 0
                for c in to_finish:
                    pt2 *= 5
                    pt2 += pt2_scoring[c]
                pt2_totals.append(pt2)
                
        print(sorted(pt2_totals))
        return sorted(pt2_totals)[int(len(pt2_totals)/2)]
        

if __name__ == '__main__':
    # d = Day10Part1("input/day10_test.txt")
    # assert d.solve() == 26397

    d2 = Day10Part1("input/day10.txt")
    answer = d2.solve()
    print(f"Answer is {answer}")
