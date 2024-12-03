# utils/parser.py
def parse_integers(input_str):
    return [int(line) for line in input_str.strip().split('\n')]
