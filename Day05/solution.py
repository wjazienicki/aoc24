from utils.input_handler import readlines
from utils.performance import timer
from collections import defaultdict
from functools import cmp_to_key

part1_path = "Day05/input.txt"
part2_path= "Day05/input.txt"

def split_rules_updates(lines):
    delimiter_index = lines.index("")
    rules = lines.copy()[:delimiter_index]
    updates = lines.copy()[delimiter_index+1:]
    return rules, updates

@timer
def part1(part1_path):
    lines = readlines(part1_path)
    rules, updates = split_rules_updates(lines)
    cant_precede = {}
    for rule in rules:
        rule = rule.split("|")
        if rule[0] not in cant_precede.keys():
            cant_precede[rule[0]] = set()
            cant_precede[rule[0]].add(rule[1])
        else:
            cant_precede[rule[0]].add(rule[1])
    correct = []
    for update in updates:
        seen = set()
        correct_flag = True
        for code in update.split(","):
            if code in cant_precede.keys() and cant_precede[code] & seen:
                seen.add(code)
                correct_flag = False
            seen.add(code)
        if correct_flag:
            correct.append(update)
    correct = [x.split(",") for x in correct]
    result = sum([int(x[int(len(x)/2)]) for x in correct])
    return result

@timer
def part2(part2_path):
    lines = readlines(part2_path)
    rules, updates = split_rules_updates(lines)

    cant_precede = defaultdict(set)
    rules = [r.split("|") for r in rules]
    rules = [[int(y) for y in x] for x in rules]
    for rule in rules:
        cant_precede[(rule[0])].add(rule[1])

    updates = [[int(x) for x in u] for u in [y.split(",") for y in updates]]
    result = 0
    for update in updates:
        s = sorted(update, key=cmp_to_key(lambda x,y: -1 if y in cant_precede[x] else 1))
        if update != s:
            result += s[len(s) // 2]
    return result


if __name__=="__main__":
    print(part1(part1_path))
    print(part2(part2_path))

 