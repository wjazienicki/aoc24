from utils.input_handler import no_linebreaks, readlines
from utils.performance import timer

part1_path = "Day04/input.txt"
part2_path= "Day04/input2.txt"


def findXMAS(x,y, grid):
    y_max = len(grid)
    x_max = len(grid[0])
    xmas_count = 0
    #N
    if y - 3 > -1:
        if grid[y-1][x] == 'M' and grid[y-2][x] == 'A' and grid[y-3][x] == "S":
            xmas_count+=1
    #NE
    if y - 3 > -1 and x + 3 < x_max:
        if grid[y-1][x+1] == 'M' and grid[y-2][x+2] == 'A' and grid[y-3][x+3] == "S":
            xmas_count+=1
    #E
    if x + 3 < x_max:
        if grid[y][x+1] == 'M' and grid[y][x+2] == 'A' and grid[y][x+3] == "S":
            xmas_count+=1
    #SE
    if y + 3 < y_max and x + 3 < x_max:
        if grid[y+1][x+1] == 'M' and grid[y+2][x+2] == 'A' and grid[y+3][x+3] == "S":
            xmas_count+=1

    #S
    if y + 3 < y_max:
        if grid[y+1][x] == 'M' and grid[y+2][x] == 'A' and grid[y+3][x] == "S":
            xmas_count+=1

    #SW
    if y + 3 < y_max and x - 3 > -1:
        if grid[y+1][x-1] == 'M' and grid[y+2][x-2] == 'A' and grid[y+3][x-3] == "S":
            xmas_count+=1

    #W
    if x - 3 > -1:
        if grid[y][x-1] == 'M' and grid[y][x-2] == 'A' and grid[y][x-3] == "S":
            xmas_count+=1

    #NW
    if y - 3 > -1 and x - 3 > -1:
        if grid[y-1][x-1] == 'M' and grid[y-2][x-2] == 'A' and grid[y-3][x-3] == "S":
            xmas_count+=1

    return xmas_count

def findMAS(x,y, grid):
    mas_count = 0
    #MAS
    if grid[y-1][x-1] == 'M' and grid[y+1][x+1] == 'S':
        if (grid[y-1][x+1] == 'S' and grid[y+1][x-1] == 'M') or (grid[y-1][x+1] == 'M' and grid[y+1][x-1] == 'S'):
            mas_count +=1
    #SAM
    elif grid[y-1][x-1] == 'S' and grid[y+1][x+1] == 'M':
        if (grid[y-1][x+1] == 'S' and grid[y+1][x-1] == 'M') or (grid[y-1][x+1] == 'M' and grid[y+1][x-1] == 'S'):
            mas_count +=1
    return mas_count

@timer
def part1(part1_path):
    grid = readlines(part1_path)
    y_min = len(grid)
    x_max = len(grid[0])
    counter = 0
    for y in range(y_min):
        for x in range(x_max):
            if grid[y][x] == "X":
                counter += findXMAS(x,y,grid)
    result = counter
    return result

@timer
def part2(part2_path):
    grid = readlines(part2_path)
    y_min = len(grid)
    x_max = len(grid[0])
    counter = 0
    for y in range(1,y_min-1):
        for x in range(1,x_max-1):
            if grid[y][x] == "A":
                counter += findMAS(x,y,grid)
    result = counter
    return result


if __name__=="__main__":
    print(part1(part1_path))
    print(part2(part2_path))

 