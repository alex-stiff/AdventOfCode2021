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
        


class Day3Part1():
    def __init__(self):
        self.input = read_input("input/day4.txt")
        self.input.append("") # For the last board
        self.boards = []
        board = []
        for line in self.input:
            if ',' in line:
                self.numbers = [int(x) for x in line.split(',')]
            elif line == "":
                if len(board) > 0:
                    self.boards.append(Board(board))
                board = []
            else:
                board.append([int(x) for x in line.split()])

        


    def solve(self):
        for number in self.numbers:
            print(f'Marking {number}')
            for board in self.boards:
                board.mark_number(number)
                if board.check_if_won():
                    print('board has won')
                    print(board.rows)
                    return board.calculate_score() * number

if __name__ == '__main__':
    d = Day3Part1()
    answer = d.solve()
    expected_answer = 4512
    assert answer == expected_answer, f"Expecting answer {expected_answer}, got {answer}"
    print(f"Answer is {answer}")
