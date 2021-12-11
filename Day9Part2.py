from helpers.input import read_input
import math
from helpers.colours import colour

class Day9Part2():
    def __init__(self, filename):
        my_input = read_input(filename)
        for x in range(len(my_input)):
            my_input[x] = [int(y) for y in my_input[x]]

        self.array = my_input
        
        # for row_index, row in enumerate(self.input):
        #     for col_index, value in enumerate(row):
        #         self.array[row_index][col_index] = int(value)

        # for row_index, row in enumerate(self.input):
        #     for col_index, value in enumerate(row):
        #         self.array[row_index][col_index] = int(value)


    def __repr__(self):
        string = ""
        for x in range(len(self.array)):
            row = self.array[x]
            l = []
            for y in range(len(row)):
                col = row[y]
                point = self.array[x][y]
                if point == 9:
                    l.append(colour.RED + str(point) + colour.END)
                elif (x, y) in self.low_points:
                    l.append(colour.GREEN + str(point) + colour.END)
                else:
                    l.append(str(point))
            string += ' '.join(l)
            string += '\n'

        return string


    def set_low_points(self):
        self.low_points = []

        for row_index in range(len(self.array)):
            for col_index in range(len(self.array[row_index])):
                if self.is_low_point(row_index, col_index):
                    self.low_points.append((row_index, col_index))

        print(self.low_points)


    def is_low_point(self, ri, ci):
        my_value = self.array[ri][ci]
        try:
            if (my_value >= self.array[ri-1][ci]):
                return False
        except IndexError as e:
            pass

        try:
            if (my_value >= self.array[ri+1][ci]):
                return False
        except IndexError as e:
            pass

        try:
            if (my_value >= self.array[ri][ci-1]):
                return False
        except IndexError as e:
            pass

        try:
            if (my_value >= self.array[ri][ci+1]):
                return False
        except IndexError as e:
            pass

        return True


    def get_basins(self):
        basins = []
        for low_point in self.low_points:
            print(low_point)
            points_in_basin = []
            new_points = [low_point]
            for x in range(1000):
                print(f'Iteration {x}')
                print(f'Fanning out from {new_points}')

                n = []
                for np in new_points:
                    for checkx, checky in (0, 1), (0, -1), (-1, 0), (1, 0):
                        x, y = np
                        if x + checkx >= 0 and x + checkx < len(self.array) and y + checky >= 0 and y + checky < len(self.array[0]):
                            poss_new = self.array[x+checkx][y+checky]
                            if poss_new != 9 and (x+checkx, y+checky) not in n and (x+checkx, y+checky) not in points_in_basin:
                                # print(f'Adding point {x+checkx}, {y+checky}')
                                n.append((x+checkx, y+checky))
                new_points = list(n)
                if len(new_points) == 0:
                    print(f'No new points in {low_point} basin, breaking')
                    break
                points_in_basin += new_points
            
            print(f'Basin from low point {low_point}: {points_in_basin}')
            basins.append(points_in_basin)
            
        return basins 

    def solve(self):
        total = 0
        self.set_low_points()
        print(self)


        basins = self.get_basins()
        for b in basins:
            print(f'Points in basin: {b}: {len(b)}')
            string = ""
            for x in range(len(self.array)):
                l = []
                row = self.array[x]
                for y in range(len(row)):
                    col = row[y]
                    point = self.array[x][y]
                    if point == 9:
                        l.append(colour.RED + str(point) + colour.END)
                    elif (x, y) in b:
                        l.append(colour.GREEN + str(point) + colour.END)
                    else:
                        l.append(str(point))
                string += ' '.join(l)
                string += '\n'
            print(string)

        prod = math.prod(sorted([len(b) for b in basins])[-3:])
        print(f'Proudct of 3 biggest basins: {prod}')
                
        
        return prod



if __name__ == '__main__':
    d = Day9Part2("input/day9_test.txt")
    answer = d.solve()
    print(f'{answer=}')
    assert answer == 1134

    d2 = Day9Part2("input/day9.txt")
    answer = d2.solve()
    print(f"Answer is {answer}")
