import time


def parseLine(line):
    dir, step, color = line.split()
    return (dir, int(step), color[1:-1])

    #A function to apply the Shoelace algorithm
def polygonArea(vertices):
    numberOfVertices = len(vertices)
    sum = 0
    for i in range(0,numberOfVertices-1):
        sum += vertices[i][0] *  vertices[i+1][1] - vertices[i][1] *  vertices[i+1][0]  
    area = abs(sum) / 2
    return area

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [parseLine(line) for line in open(self.filename).read().split("\n")]
        self.dirs = {"L":(-1, 0), "R":(1, 0), "D": (0, 1), "U": (0, -1)}
        self.perimeter = set()
        
    def part1(self):
        x, y = 0, 0
        maxX = -float("inf")
        maxY = -float("inf")
        minX = float("inf")
        minY = float("inf")
        for dir, step, color in self.data:
            dx, dy = self.dirs[dir]
            
            for _ in range(step):
                x, y = x + dx, y + dy
                maxX = max(maxX, x)
                maxY = max(maxY, y)
                minX = min(minX, x)
                minY = min(minY, y)
                self.perimeter.add((x, y))
            
        s = 0
        for y in range(minY, maxY + 1):
            for x in range(minX, maxX + 1):
                if (x, y) in self.perimeter:
                    s += 1
                elif self.isInside(x, y, minX):
                    s += 1
        self.write(minX, maxX, minY, maxY)
        return s
    
    def write(self, minX, maxX, minY, maxY):
        grid = [["#" if (x, y) in self.perimeter else "." for x in range(minX, maxX + 1)] for y in range(minY, maxY + 1)]
        with open("out.txt", "w") as f:
            for line in grid:
                f.write("".join(line) + "\n")
                    
                    
    def isInside(self, x, y, minX):
        crossings = 0
        while x >= minX:
                #L
            if (x, y) in self.perimeter and (x + 1, y) in self.perimeter and (x, y - 1) in self.perimeter:
                crossings += 1
                #J
            elif (x, y) in self.perimeter and (x - 1, y) in self.perimeter and (x, y - 1) in self.perimeter:
                crossings += 1
                #| 
            elif (x, y) in self.perimeter and (x, y - 1) in self.perimeter:
                crossings += 1
            x -= 1
        return crossings % 2 == 1
    
    def part2(self):
        corners = [(0, 0)]
        extra = 1
        x, y = 0, 0
        dirs = {0: "R", 1: "D", 2: "L", 3: "U"}
        for _, *_, hex in self.data:
            step = int(hex[1:6], 16)
            dir_int = int(hex[6:], 16)
            dir = dirs[dir_int]
            dx, dy = self.dirs[dir]
            x, y = x + dx * step, y + dy * step
            corners.append((x, y))
            if dir == "D" or dir == "R":
                
                for _ in range(step):
                    extra += 1
            
        corners = corners[:-1]
        return polygonArea(corners) + extra
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}\n")
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()