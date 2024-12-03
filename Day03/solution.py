import re
from utils.input_handler import no_linebreaks
from utils.performance import timer

part1_path = "Day03/input.txt"
part2_path="Day03/input2.txt"

@timer
def part1(part1_path):
    txt = no_linebreaks(part1_path)
    pattern = r"mul\((-?\d+),(-?\d+)\)"
    matches = re.findall(pattern, txt)
    muls = [(int(x), int(y)) for x, y in matches]
    result = sum([x[0]*x[1] for x in muls])
    return result

@timer
def part2(part2_path):
    txt = no_linebreaks(part2_path)
    pattern = r"mul\((-?\d+),(-?\d+)\)|don't\(\)|do\(\)"
    matches = re.finditer(pattern, txt)
    execute = True
    symbols = []
    for match in matches:
        if match.group(1) and match.group(2):
            symbols.append((int(match.group(1)), int(match.group(2))))
        elif match.group(0) == "don't()":
            symbols.append("don't()")
        elif match.group(0) == "do()":
            symbols.append("do()")
    
    muls=[]
    for member in symbols:
        if member == "don't()":
            execute = False
        elif member == "do()":
            execute = True
        else:
            if execute:
                muls.append(member[0] * member[1])
    result = sum(muls)
    return result


if __name__=="__main__":
    print(part1(part1_path))
    print(part2(part2_path))

 