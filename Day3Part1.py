from helpers.input import read_input
import math

class Day3Part1():
    def __init__(self):
        self.input = read_input("input/day3.txt")


    def most_common_nth(self, n):
        print(sum([int(i[n]) for i in self.input]))
        if sum([int(i[n]) for i in self.input]) > len(self.input)/2:
            return "1"
        else:
            return "0"


    def solve(self):
        number=""
        for x in range(len(self.input[0])):
            number += self.most_common_nth(x)
        gamma = int(number, 2)
        epsilon = int(math.pow(2, len(self.input[0])) - 1) - gamma
        return gamma, epsilon, gamma*epsilon


if __name__ == '__main__':
    d = Day3Part1()
    answer = d.solve()
    print(f"Answer is {answer}")
