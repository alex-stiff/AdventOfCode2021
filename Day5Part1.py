from helpers.input import read_input
import math
import sys

class Board():
    def __init__(self, rows):
        self.rows = rows
        self.original_score = self.calc_current_score()


    def calc_current_score(self):
        score = 0
        for row in self.rows:
            score += sum([x for x in row if x != 'X'])
        
        return score

    def mark_number(self, number):
        print(self.rows)
        for row in self.rows:
            try:
                index = row.index(number)
                row[index] = 'X'
            except:
                pass
        print(self.rows)

    def check_if_won(self):
        for row in self.rows:
            if all([n == 'X' for n in row]):
                return True
        for column in range(len(row)):
            if all([row[column] == 'X' for row in self.rows]):
                return True

        return False
    
    def calculate_score(self):
        return self.calc_current_score()
        


class Day5Part1():
    def __init__(self):
        self.load_input()


    def load_input(self):
        self.input = read_input("input/day5.txt")
        self.coordinates = [p.split(' -> ') for p in self.input]


    def get_points_between(self, points):
        first = [int(x) for x in points[0].split(',')]
        second = [int(x) for x in points[1].split(',')]
        points = []
        print(first, second)

        if first[0] == second[0]:
            print('Vertical line')
            if first[1] > second[1]:
                bigger = first[1]
                smaller = second[1]
            else:
                bigger = second[1]
                smaller = first[1]
            points = [f'{first[0]}-{x}' for x in range(smaller, bigger + 1)]
        elif first[1] == second[1]:
            print('Horizontal line')
            if first[0] > second[0]:
                bigger = first[0]
                smaller = second[0]
            else:
                bigger = second[0]
                smaller = first[0]
            points = [f'{x}-{first[1]}' for x in range(smaller, bigger + 1)]
        else:
            print('Diagonal line')
            x_step = y_step = -1

            if second[0] > first[0]:
                x_step = 1
            if second[1] > first[1]:
                y_step = 1

            x_values = [x for x in range(first[0], second[0] + x_step, x_step)]
            y_values = [y for y in range(first[1], second[1] + y_step, y_step)]
            points = [f'{x_values[i]}-{y_values[i]}' for i in range(len(x_values))]
            
        print(f'Points are {points}')
        
        return points
            


    def solve(self):
        d = dict()
        for i in self.coordinates:
            for points in self.get_points_between(i):
                try:
                    d[points] = d[points] + 1
                except:
                    d[points] = 1
        print(len([k for k, v in d.items() if v > 1]))

if __name__ == '__main__':
    d = Day5Part1()
    answer = d.solve()
    print(f"Answer is {answer}")
