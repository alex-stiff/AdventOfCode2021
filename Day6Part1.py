from helpers.input import read_input
import math
import sys

class Fish():
    def __init__(self, timer):
        self.timer = timer


    def spawn_new(self):
        f = Fish(8)


    def age(self):
        if self.timer == 0:
            f = Fish(8)
            self.timer = 6
            return f
        else:
            self.timer -= 1
        
        return None


class Day6Part1():
    def __init__(self):
        self.load_input()
        self.fish = [Fish(int(x)) for x in self.input[0].split(',')]


    def load_input(self):
        self.input = read_input("input/day6.txt")


    def solve(self):
        days = 80
        for x in range(1, days+1):
            new_fishes = []
            for f in self.fish:
                newf = f.age()
                if newf is not None:
                    new_fishes.append(newf)
            print('Adding new fish')
            self.fish = self.fish + new_fishes

            print(f'after {x} days, fish are: {[x.timer for x in self.fish]}')
        
        print(f'{len(self.fish)} fish after {days} days')

        return -1
if __name__ == '__main__':
    d = Day6Part1()
    answer = d.solve()
    print(f"Answer is {answer}")
