from helpers.input import read_input
import collections

class Day7Part2():
    def __init__(self):
        self.input = [int(k) for k in read_input("input/day7.txt")[0].split(',')]
        self.numbers = collections.Counter(self.input)
        self.fuel_distances = {
            x: sum([k for k in range(x+1)]) for x in range(max(self.input)+1)
        }


    def solve(self):
        min_distance = None
        for x in range(min(self.input), max(self.input)+1):
            distance = 0
            for k, v in self.numbers.items():
                distance += self.fuel_distances[abs(x - k)] * v
            if min_distance is None or distance < min_distance:
                min_distance = distance
            
        return min_distance

if __name__ == '__main__':
    d = Day7Part2()
    answer = d.solve()
    print(f"Answer is {answer}")
