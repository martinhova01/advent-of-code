def part1(inputfilename):
    data = [list(x) for x in open(inputfilename).read().split("\n")]
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])
    lowPoints = []
    
    for i in range(len(data)):
        for j in range(len(data[i])):
            if isLowPoint(i, j, data):
                lowPoints.append(1 + data[i][j])
                
                
    print(lowPoints)
    return sum(lowPoints)


def isLowPoint(i, j, data):
    for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        if i + x < 0 or j + y < 0 or i + x >= len(data) or j + y >= len(data[i]):
            continue
        if(data[i][j] >= data[i + x][j + y]):
            return False
        
    return True
    

def part2(inputfilename):
    
    return -1


def main(test = False):
    if test:
        filename = '21/day9/testinput.txt'
    else:
        filename = '21/day9/input.txt'
        
    print(f"part 1 : {part1(filename)}")
    print(f"part 2 : {part2(filename)}")
    
    
main()