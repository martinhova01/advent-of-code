
def part1(filename):
    points = [(int(line.split(",")[0]), int(line.split(",")[1])) for line in open(filename).read().split("\n\n")[0].split("\n")]
    instructions = [(line.split("=")[0][-1], int(line.split("=")[1])) for line in open(filename).read().split("\n\n")[1].split("\n")]
    
    
    instruction = instructions[0]
    foldX = True if instruction[0] == "x" else False
    value = instruction[1]
    
    fold(points, foldX, value)
    points = set(points)
       
    return len(points)
    
    
    
def fold(points, foldX, value):
    if foldX:
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            if x < value:
                continue
            dist = x - value
            points[i] = (value - dist, y)
    else:
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            if y < value:
                continue
            dist = y - value
            points[i] = (x, value - dist)
                
        
            
def getString(points):
    maxX = max(points, key= lambda p : p[0])[0]
    maxY = max(points, key= lambda p : p[1])[1]
    
    s = ""
    for i in range(maxY + 1):
        for j in range(maxX + 1):
            s += "#" if (j, i) in points else " "
        s += "\n"
    return s

def part2(filename):
    points = [(int(line.split(",")[0]), int(line.split(",")[1])) for line in open(filename).read().split("\n\n")[0].split("\n")]
    instructions = [(line.split("=")[0][-1], int(line.split("=")[1])) for line in open(filename).read().split("\n\n")[1].split("\n")]
    
    for instruction in instructions:
        foldX = True if instruction[0] == "x" else False
        value = instruction[1]
        fold(points, foldX, value)
    
    points = set(points)
    
    return getString(points)
    
    
def main(test = False):
    filename = "testinput.txt" if test else "input.txt"    
    print(f"part 1 : {part1(filename)}")
    print(f"part 2 : \n{part2(filename)}")
    
main()