from helpers.input import read_input

class Day8Part1():
    def __init__(self):
        self.input = read_input("input/day8.txt")
        

    def get_answer(self, line):
        #   1
        # 2   3
        #   4
        # 5   6
        #   7

        # 2: 1
        # 3: 7
        # 4: 4
        # 5: 2, 3, 5
        # 6: 6, 9, 0
        # 7: 8
        split_input = line.split('|')
        hints = [''.join(sorted(x)) for x in split_input[0].split()]
        num_map = {x: 'abcdefg' for x in range(10)}
        for h in hints:
            if len(h) == 2:
                num_map[1] = h
            elif len(h) == 3:
                num_map[7] = h
            elif len(h) == 4:
                num_map[4] = h
            elif len(h) == 7:
                num_map[8] = h
        
        print(hints, num_map)

        # # Figure out segments
        # six_nine_zero = [h for h in hints if len(h) == 6]
        # print(f'6s/9s/0s: {six_nine_zero}')
        # two_three_five = [h for h in hints if len(h) == 5]
        # print(f'2s/3s/5s: {two_three_five}')

        # 9 = 4 + 7
        

        # still need 2, 3, 5, 6, 0, 9
        # have 1, 4, 7, 8

        # bottom_left = [x for x in num_map[8] if x not in num_map[9]]
        # print(f'bottom left is {bottom_left}')

        # print(num_map[9])
        return [num_map[1], num_map[7], num_map[4], num_map[8]]
    

    def output_numbers(self, numbermap, line):
        split_input = line.split('|')
        numbers = split_input[1].split()
        print(numbers)

    def count_outputs_matching(self, matches, line):
        split_input = line.split('|')
        numbers = [''.join(sorted(x)) for x in split_input[1].split()]
        print(matches, numbers)
        total = 0
        for i in matches:
            total += numbers.count(i)
        return total

    def solve(self):
        total = 0
        for line in self.input:
            onefourseveneight = self.get_answer(line)
            total += self.count_outputs_matching(onefourseveneight, line)
        return total

if __name__ == '__main__':
    d = Day8Part1()
    answer = d.solve()
    print(f"Answer is {answer}")
