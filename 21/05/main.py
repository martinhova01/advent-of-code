import math
from pathlib import Path
def solve(inputfilename, part2 = False):
    data = [[0 for i in range(1000)] for x in range(1000)]
    with open(inputfilename) as f:
        for line in f.readlines():
            x1 = int(line.split(" -> ")[0].split(",")[0])
            x2 = int(line.split(" -> ")[1].split(",")[0])
            y1 = int(line.split(" -> ")[0].split(",")[1])
            y2 = int(line.split(" -> ")[1].split(",")[1])
            
                #horizontal line
            if x1 == x2:
                for i in range(min(y1, y2), max(y1,y2) + 1):
                    data[i][x1] += 1
                #vertical line
            elif y1 == y2:
                for i in range(min(x1, x2), max(x1, x2) + 1):
                    data[y1][i] += 1
            elif part2:
                #part 2 diagonal line
                xCounter = 0
                yCounter = 0
                if x1 < x2 and y1 < y2:
                    xCounter = 1
                    yCounter = 1
                elif x1 < x2 and y1 > y2:
                    xCounter = 1
                    yCounter = -1
                elif x1 > x2 and y1 < y2:
                    xCounter = -1
                    yCounter = 1
                elif x1 > x2 and y1 > y2:
                    xCounter = -1
                    yCounter = -1
                
                i = -1
                while x1 + (i * xCounter) != x2:
                    i += 1
                    data[y1 + i * yCounter][x1 + i * xCounter] += 1
                
        
    
    result = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] > 1:
                result += 1
                
    return result
            
            



def main(test = False):
    if test:
        filename = str(Path(__file__).parent / "testinput.txt")
    else:
        filename = str(Path(__file__).parent / "input.txt")
        
    print(f"part 1 : {solve(filename, False)}")
    print(f"part 2 : {solve(filename, True)}")
    
    
main()