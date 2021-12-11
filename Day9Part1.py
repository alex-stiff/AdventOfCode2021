from helpers.input import read_input
import math

class Day9Part1():
    def __init__(self, filename):
        self.input = read_input(filename)
        self.array = {x: {} for x in range(len(self.input))}
        for row_index, row in enumerate(self.input):
            for col_index, value in enumerate(row):
                self.array[row_index][col_index] = int(value)


    def is_low_point(self, ri, ci):
        my_value = self.array[ri][ci]
        try:
            if (my_value >= self.array[ri-1][ci]):
                return False
        except KeyError as e:
            pass

        try:
            if (my_value >= self.array[ri+1][ci]):
                return False
        except KeyError as e:
            pass

        try:
            if (my_value >= self.array[ri][ci-1]):
                return False
        except KeyError as e:
            pass

        try:
            if (my_value >= self.array[ri][ci+1]):
                return False
        except KeyError as e:
            pass

        return True

    def get_low_points(self):
        for row_index in range(len(self.array)):
            for col_index in range(len(self.array[row_index])):
                if self.is_low_point(row_index, col_index):
                    yield (row_index, col_index)


    def solve(self):
        total = 0

        for x, y in self.get_low_points():
            print(f'{x=}, {y=}, {self.array[x][y]}')
            total += (self.array[x][y] + 1)

        return total
        


if __name__ == '__main__':
    d = Day9Part1("input/day9_test.txt")
    assert d.solve() == 15

    d2 = Day9Part1("input/day9.txt")
    answer = d2.solve()
    assert answer == 516
    print(f"Answer is {answer}")
