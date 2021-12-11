from helpers.input import read_input
import math
from helpers.colours import colour

class Octopus():
    def __init__(self, energy, row, col):
        self.energy = energy
        self.flashed = False
        self.checked_adjacent = False
        self.x = row
        self.y = col

    def advance(self):
        if self.flashed:
            return

        self.energy += 1
        
        if self.energy > 9:
            self.flashed = True
        
        

    def __str__(self):
        if self.checked_adjacent:
            return colour.GREEN + str(self.energy) + colour.END
        elif self.flashed:
            return colour.YELLOW + str(self.energy) + colour.END
        else:
            return str(self.energy)

class Day11Part1():
    def __init__(self, filename):
        self.input = read_input(filename)
        self.octopuses = [[None]*10 for x in range(10)]
        for row_index, row in enumerate(self.input):
            for col_index, value in enumerate(row):
                self.octopuses[row_index][col_index] = Octopus(int(value), row_index, col_index)

    def print_grid(self):
        pass
        for x in range(10):
            print(' '.join([str(self.octopuses[x][y]) for y in range(10)]))
        print()

    def get_flashed(self):
        number_flashed = 0

        for y in self.octopuses:
            number_flashed += len([x for x in y if x.flashed])

        return number_flashed

    def advance_adjacent(self, x, y):
        if self.octopuses[x][y].checked_adjacent:
            return

        self.octopuses[x][y].checked_adjacent = True
        for checkx, checky in (0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1):
            if x + checkx >= 0 and x + checkx < 10 and y + checky >= 0 and y + checky < 10:
                self.octopuses[x+checkx][y+checky].advance()

    def reset_to_zero(self):
        for x in range(10):
            for y in range(10):
                self.octopuses[x][y].flashed = False
                self.octopuses[x][y].checked_adjacent = False
                if self.octopuses[x][y].energy > 9:
                    self.octopuses[x][y].energy = 0

    def advance(self):
        self.print_grid()
        
        # Advance everything by 1 step
        for x in range(10):
            for y in range(10):
                self.octopuses[x][y].advance()
        print('Everything has flashed normally')
        self.print_grid()
        flashed = self.get_flashed()
        
        # Keep advancing octopuses next to others until no new ones
        for _ in range(30):
            for x in range(10):
                for y in range(10):
                    if self.octopuses[x][y].flashed:
                        self.advance_adjacent(x, y)
            
            
            new_flashed = self.get_flashed()
            print(f'{flashed=}, {new_flashed=}')
            if new_flashed == flashed:
                self.reset_to_zero()
                self.print_grid()
                return flashed
            
            flashed = new_flashed
        
        


    def solve(self):
        flashes = 0
        for iteration in range(100):
            print(f'{iteration=}')
            flashes += self.advance()
            print(f'{flashes=}')

        return flashes
    
    def solve2(self):
        flashes = 0
        for iteration in range(1000):
            new_flashes = self.advance()
            flashes += new_flashes
            if new_flashes == 100:
                return iteration + 1
        
            
        
        return flashes


if __name__ == '__main__':
    d = Day11Part1("input/day11_test.txt")
    assert d.solve() == 1656

    d2 = Day11Part1("input/day11.txt")
    answer = d2.solve()
    print(f"Answer is {answer}")

    d2p2 = Day11Part1("input/day11_test.txt")
    d2p2answer = d2p2.solve2()
    assert d2p2answer == 195

    d2p22 = Day11Part1("input/day11.txt")
    d2p2answer2 = d2p22.solve2()
    print(d2p2answer2)

    
    


