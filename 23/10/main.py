from collections import deque
import time

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [[x for x in line] for line in open(self.filename).read().split("\n")]
        self.startPos = self.findStartPos()
        self.startSymbol = "F" if test else "|"
        dirs = {"NORTH": (0, -1), "SOUTH": (0, 1), "EAST": (1, 0), "WEST": (-1, 0)}
        self.pipes = {
                        "|": {dirs["NORTH"], dirs["SOUTH"]},
                        "-": {dirs["EAST"], dirs["WEST"]},
                        "L": {dirs["NORTH"], dirs["EAST"]},
                        "J": {dirs["NORTH"], dirs["WEST"]},
                        "7": {dirs["SOUTH"], dirs["WEST"]},
                        "F": {dirs["SOUTH"], dirs["EAST"]}
                    }
        
    def findStartPos(self):
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                if self.data[y][x] == "S":
                    return (x, y)
        
    def part1(self):
        return int(len(self.getCycle()) / 2)     
                
    def getCycle(self):
        q = deque()
        visited = {self.startPos}
        for dir in self.pipes[self.startSymbol]:
            q.append((self.startPos[0] + dir[0], self.startPos[1] + dir[1]))
            
        d = 0
        while q:
            d += 1
            x, y = q.popleft()
            visited.add((x, y))
            c = self.data[y][x]
            for dir in self.pipes[c]:
                nextX = x + dir[0]
                nextY = y + dir[1]
                if (nextX, nextY) in visited:
                    continue
                q.append((nextX, nextY))
        
        return visited
    
    def containsPoint(self, x, y, cycle):
        crossings = 0
        while x > 0 and y > 0 and y < len(self.data):
            if (x - 1, y) not in cycle:
                x -= 1
                continue
            pipe = self.data[y][x - 1]
            if pipe == "|" or pipe == "L" or pipe == "J":
                crossings += 1
            x -= 1
        return crossings % 2 == 1
    
        #A point is inside the cycle if you have to cross a odd number of edged to get to the outside of the graph
    def part2(self):
        self.data[self.startPos[1]][self.startPos[0]] = self.startSymbol # replace S with correct symbol
        s = 0
        cycle = self.getCycle()
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                if (x, y) in cycle:
                    continue
                if self.containsPoint(x, y, cycle):
                    s += 1      
        return s   
    
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