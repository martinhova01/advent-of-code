def getLowPoints(inputfilename):
    data = [list(x) for x in open(inputfilename).read().split("\n")]
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])
    lowPoints = []
    
    for i in range(len(data)):
        for j in range(len(data[i])):
            if isLowPoint(i, j, data):
                lowPoints.append((j, i))
    
    sum = 0
    for x, y in lowPoints:
        sum += 1 + data[y][x]
    
    return (sum, lowPoints)

def isLowPoint(i, j, data):
    for x, y in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        if i + x < 0 or j + y < 0 or i + x >= len(data) or j + y >= len(data[i]):
            continue
        if(data[i][j] >= data[i + x][j + y]):
            return False
    return True
    

def part2(inputfilename):
    data = [list(x) for x in open(inputfilename).read().split("\n")]
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])
            
    lowPoints = getLowPoints(inputfilename)[1]
    
    basins = [[-1 for _ in range(len(x))] for x in data] #a 2d list where basins[y][x] = i mean (x, y) is in basin i.
    
    
    for i in range(len(lowPoints)):
        x = lowPoints[i][0]
        y = lowPoints[i][1]
        setBasin(i, x, y, basins, data)
        
    basinSizes = [0 for _ in range(len(lowPoints))]
    
    for y in range(len(basins)):
        for x in range(len(basins[y])):
            if basins[y][x] == -1:
                continue
            basinSizes[basins[y][x]] += 1
            
    basinSizes.sort(reverse=True)
    
    prod = 1
    for i in range(3):
        prod *= basinSizes[i]
        
    return prod
        
        
    #i -> basinnumber
    #x -> x-coordinate
    #y -> y-coordinate
    #basins -> 2d list of basinnumbers
def setBasin(i, x, y, basins, data):
    if x >= len(data[0]) or x < 0 or y >= len(data) or y < 0:
        return
    if data[y][x] == 9 or basins[y][x] != -1:
        return 
    basins[y][x] = i
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for (offsetX, offsetY) in directions:
        setBasin(i, x + offsetX, y + offsetY, basins, data)
        
        
def main(test = False):
    if test:
        filename = '21/day9/testinput.txt'
    else:
        filename = '21/day9/input.txt'
        
    print(f"part 1 : {getLowPoints(filename)[0]}")
    print(f"part 2 : {part2(filename)}")
    
    
main()