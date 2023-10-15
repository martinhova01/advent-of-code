
def part1(filename):
    data = [[int(y) for y in list(x)] for x in open(filename).read().split("\n")]
    counter = 0
    for _ in range(100):
        counter += step(data)

    return counter
    
def step(data):
    flashes = []
    counter = 0
    
        #increment all values and flash if needed
    for i in range(10):
        for j in range(10):
            data[i][j] += 1
            if data[i][j] > 9 and (i, j) not in flashes:
                flashes.append((i, j))
                counter += flash(data, flashes, counter, i, j)
         
         #set flashed points to 0       
    for (i, j) in flashes:
        data[i][j] = 0
                       
    return counter
                
def flash(data, flashes, counter, i, j):
    counter = 1
    directions = {(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)}
    for (i_offset, j_offset) in directions:
        x = i + i_offset
        y = j + j_offset
        if x < 0 or x > 9 or y < 0 or y > 9:
            continue
        data[x][y] += 1
        if data[x][y] > 9 and (x, y) not in flashes:
            flashes.append((x, y))
            counter += flash(data, flashes, counter, x, y)
            
    return counter

def part2(filename):
    data = [[int(y) for y in list(x)] for x in open(filename).read().split("\n")]
    
    i = 0
    while step(data) != 100:
        i += 1
    
    return i + 1




def main(test = False):
    filename = "testinput.txt" if test else "input.txt"    
    print(f"part 1 : {part1(filename)}")
    print(f"part 2 : {part2(filename)}")
    
main()