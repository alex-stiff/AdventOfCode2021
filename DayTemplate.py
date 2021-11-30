from helpers.input import read_input

class DayXpartY():
    def __init__(self):
        self.input = read_input("input/dayX.txt")


    def solve(self):
        pass

if __name__ == '__main__':
    dayXpartY = DayXpartY()
    answer = dayXpartY.solve()
    print(f"Answer is {answer}")
