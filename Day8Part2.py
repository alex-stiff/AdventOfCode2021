from helpers.input import read_input
import collections

class Day8Part2():
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
        solved_letters = [None]*7
        split_input = line.split('|')
        hints = [''.join(sorted(x)) for x in split_input[0].split()]
        remaining_hints = [''.join(sorted(x)) for x in split_input[0].split()]
        num_map = {x: None for x in range(10)}
        print(hints)
        for h in hints:
            if len(h) == 2:
                num_map[1] = h
                remaining_hints.remove(h)
            elif len(h) == 3:
                num_map[7] = h
                remaining_hints.remove(h)
            elif len(h) == 4:
                num_map[4] = h
                remaining_hints.remove(h)
            elif len(h) == 7:
                num_map[8] = h
                remaining_hints.remove(h)

        # still need 2, 3, 5, 6, 0, 9
        # have 1, 4, 7, 8

        # How many times does each segment appear in the remaining numbers
        # 1: 6, 2: 4
        # 3: 4, 4: 5
        # 5: 3, 6: 5
        # 7: 6
        #
        # So we can work out bottom left line by seeing what has 3
        mycount = collections.Counter(''.join(remaining_hints))
        solved_letters[4] = [k for k,v in mycount.items() if v == 3][0]

        # we can figure out what 9 is by doing 8 - bottom left
        num_map[9] = ''.join(sorted([l for l in num_map[8] if l != solved_letters[4]]))
        remaining_hints.remove(num_map[9])

        # How many times does each segment appear in the remaining numbers
        # 1: 5, 2: 3
        # 3: 3, 4: 4
        # 5: 3, 6: 4
        # 7: 5

        # still need 2, 3, 5, 6, 0
        # have 1, 4, 7, 8, 9
        counters = collections.Counter(''.join(remaining_hints))
        possible_letters_for_4_or_6 = [k for k,v in counters.items() if v == 4]
        print(possible_letters_for_4_or_6)
        # segment 6 is in 1
        solved_letters[5] = [l for l in possible_letters_for_4_or_6 if l in num_map[1]][0]
        solved_letters[3] = [l for l in possible_letters_for_4_or_6 if l not in num_map[1]][0]
        num_map[0] = ''.join(sorted([l for l in num_map[8] if l != solved_letters[3]]))
        remaining_hints.remove(num_map[0])

        # still need 2, 3, 5, 6
        # have 1, 4, 7, 8, 9, 0
        # How many times does each segment appear in the remaining numbers
        # 1: 4, 2: 2
        # 3: 2
        # 7: 4

        # 8 - 7 + 4 + bottom left = bottom
        bl_plus_4 = ''.join(set(solved_letters[4] + num_map[4] + num_map[7]))
        solved_letters[6] = [x for x in num_map[8] if x not in bl_plus_4][0]

        print(f'{solved_letters[6]=}')

        # At this point unknown letters are 0, 1, 2
        # Numbers to find are 2, 3, 5, 6
        # One with length 6 is the 6
        num_map[6] = [x for x in remaining_hints if len(x) == 6][0]
        remaining_hints.remove(num_map[6])

        # At this point unknown letters are 0, 1, 2
        # Numbers to find are 2, 3, 5
        # 6 minus bottom left (solved[4]) is 5
        num_map[5] = ''.join([x for x in num_map[6] if x != solved_letters[4]])
        remaining_hints.remove(num_map[5])

        # Numbers to find are 2, 3
        # 3 only has 1 less letter than 9
        # 2 has 2 less letters than 9
        for i in remaining_hints:
            # Which are in 9
            if all([letter in num_map[9] for letter in i]):
                # This one is the 3
                num_map[3] = i
            else:
                num_map[2] = i

        
        return num_map
    
    def count_outputs_matching(self, matches, line):
        split_input = line.split('|')
        numbers = [''.join(sorted(x)) for x in split_input[1].split()]
        total = ""
        for n in numbers:
            for k, v in matches.items():
                if v == n:
                    total += str(k)
        return int(total)

    def solve(self):
        total = 0
        for line in self.input:
            num_map = self.get_answer(line)
            total += self.count_outputs_matching(num_map, line)
        return total

if __name__ == '__main__':
    d = Day8Part2()
    answer = d.solve()
    print(f"Answer is {answer}")
