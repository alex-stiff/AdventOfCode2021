def read_input(filename):
    with open(filename, 'r') as f:
        return f.read().split()

def read_input_int(filename):
    return [int(x) for x in read_input(filename)]