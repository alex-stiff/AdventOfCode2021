from helpers.input import read_input

class Signal(str):
    def number_of_intersections(self, other):
        joint = self + other
        intersections = len(joint) - len(set(joint))

        return intersections

    def contains(self, other):
        return self.number_of_intersections(other) == len(other)


class Day8Part2():
    def __init__(self):
        self.input = read_input("input/day8.txt")
        self.num_map = {x: None for x in range(10)}


    def find_with_length(self, patterns, length):
        matching_patterns = []
        for pattern in patterns:
            if len(pattern) == length:
                matching_patterns.append(pattern)

        return matching_patterns


    def get_number_map(self, signal_patterns):
        number_map = {}

        # Easy ones
        number_map[1] = self.find_with_length(signal_patterns, 2)[0]
        number_map[4] = self.find_with_length(signal_patterns, 4)[0]
        number_map[7] = self.find_with_length(signal_patterns, 3)[0]
        number_map[8] = self.find_with_length(signal_patterns, 7)[0]

        # With length 5
        for f in self.find_with_length(signal_patterns, 5):
            if f.number_of_intersections(number_map[7]) == len(number_map[7]):
                number_map[3] = f
            else:
                if f.number_of_intersections(number_map[4]) == 3:
                    number_map[5] = f
                else:
                    number_map[2] = f
        
        # With length 6
        for f in self.find_with_length(signal_patterns, 6):
            if f.number_of_intersections(number_map[4]) == len(number_map[4]):
                number_map[9] = f
            else:
                if f.number_of_intersections(number_map[7]) == len(number_map[7]):
                    number_map[0] = f
                else:
                    number_map[6] = f

        return {''.join(sorted(v)): k for k, v in number_map.items()}

    def decode(self, line):
        signal_patterns = [Signal(x) for x in line.split('|')[0].split()]
        output_values = [''.join(sorted(x)) for x in line.split('|')[1].split()]

        number_map = self.get_number_map(signal_patterns)
        print(number_map)
        output = "".join([str(number_map[code]) for code in output_values])

        return int(output)

    def solve(self):
        total = sum([self.decode(line) for line in self.input])
        return total

if __name__ == '__main__':
    d = Day8Part2()
    answer = d.solve()
    print(f"Answer is {answer}")
