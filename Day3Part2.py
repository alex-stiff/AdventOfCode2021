from helpers.input import read_input

class Day3Part1():
    def __init__(self):
        self.input = read_input("input/day3.txt")
        self.report_number_length = len(self.input[0])


    def most_common_nth(self, numbers, n):
        if sum([int(i[n]) for i in numbers]) < len(numbers)/2:
            return "0"
        else:
            return "1"


    def most_uncommon_nth(self, numbers, n):
        if sum([int(i[n]) for i in numbers]) < len(numbers)/2:
            return "1"
        else:
            return "0"


    def get_oxygen_generator_rating(self):
        numbers = list(self.input)
        for x in range(self.report_number_length):
            if len(numbers) == 1:
                break
            most_common = self.most_common_nth(numbers, x)
            numbers = self.get_numbers_where_nth_is(numbers, most_common, x)

        return int(numbers[0], 2)


    def get_co2_scrubber_rating(self):
        numbers = list(self.input)
        for x in range(self.report_number_length):
            if len(numbers) == 1:
                break
            most_common = self.most_uncommon_nth(numbers, x)
            numbers = self.get_numbers_where_nth_is(numbers, most_common, x)

        return int(numbers[0], 2)


    def get_numbers_where_nth_is(self, numbers, most_common, n):
        return [num for num in numbers if num[n] is most_common]

    
    def solve(self):
        ogr = self.get_oxygen_generator_rating()
        csr = self.get_co2_scrubber_rating()
        life_support_rating = ogr * csr
        return life_support_rating

        

if __name__ == '__main__':
    d = Day3Part1()
    answer = d.solve()
    print(f"Answer is {answer}")
