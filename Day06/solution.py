from utils.input_handler import readlines
from utils.performance import timer
import itertools

part1_path = "Day06/input.txt"
part2_path= "Day06/input.txt"

def inside(grid_position, row_num, col_num):
    return (0 <=grid_position[0] < row_num) & (0 <=grid_position[1] < col_num)

def count_spots(grid, start, obstructions, row_num, col_num):
    directions = [(-1, 0), (0,1),(1,0),(0,-1)]
    cycle = itertools.cycle(directions)
    spotted = [(start)]
    position = start
    direction = next(cycle)
    while inside(position, row_num, col_num):
        next_pos = (position[0] + direction[0], position[1] + direction[1])
        if next_pos in obstructions:
            direction = next(cycle)
        if position not in spotted:
            spotted.append(position)
        position = (position[0] + direction[0], position[1] + direction[1])
    return len(spotted)

@timer
def part1(part1_path):
    grid = readlines(part1_path)
    row_num = len(grid)
    col_num = len(grid[0])
    #find obstructions and starting position
    obstructions = []
    found = False
    for row in range(row_num):
        for col in range(col_num):
            if grid[row][col] == "#":
                obstructions.append((row,col))
            elif not found and grid[row][col] == "^":
                found = True
                start = (row, col)
    
    return count_spots(grid,start,obstructions,row_num,col_num)


@timer
def part2(part2_path):

    grid = readlines(part2_path)
    row_num = len(grid)
    col_num = len(grid[0])
    #find obstructions and starting position
    obstructions = []
    found = False
    possible_obstructions = []
    for row in range(row_num):
        for col in range(col_num):
            if grid[row][col] == "#":
                obstructions.append((row,col))
            elif not found and grid[row][col] == "^":
                found = True
                start = (row, col)
            else:
                possible_obstructions.append((row,col))
    loops = 0
    for case in possible_obstructions:
        print(case)
        temp_obstructions = obstructions.copy()
        temp_obstructions.append(case)
        directions = [(-1, 0), (0,1),(1,0),(0,-1)]
        cycle = itertools.cycle(directions)
        position = start
        direction = next(cycle)
        spotted = [(start)]
        spotted_directions = [direction]
        while inside(position, row_num, col_num):
            next_pos = (position[0] + direction[0], position[1] + direction[1])
            if position not in spotted:
                spotted.append(position)
                spotted_directions.append(direction)
            else:
                i = spotted.index(position)
                if direction == spotted_directions[i] and i != 0:
                    print("loop!")
                    loops+=1
                    break
            if next_pos in temp_obstructions:
                direction = next(cycle)               
            position = (position[0] + direction[0], position[1] + direction[1])
    return loops

if __name__=="__main__":
    print(part1(part1_path))
    print(part2(part2_path))

 