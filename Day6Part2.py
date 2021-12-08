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


class Day6Part2():
    def __init__(self):
        self.input = read_input("input/day6.txt")
        self.fish = [self.input[0].count(str(i)) for i in range(9)]


    def solve(self):
        days = 30
        for x in range(1, days+1):
            pass


    def age_all_fish(self):
        new_fish = dict()
        for x in range(1,9):
            new_fish[x - 1] = self.fish.get(x)

        try:
            new_fish[8] = new_fish[8] + self.fish.get(0)
        except:
            new_fish[8] = self.fish.get(-1)
        print(f'old fish: {self.fish}, new fish: {new_fish}')


        
if __name__ == '__main__':
    d = Day6Part2()
    # answer = d.solve()
    print(f"Answer is {answer}")
