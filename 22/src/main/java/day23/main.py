import time

import sys
sys.path.append("../../../../..")
from utils import adjacent8

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.elves = self.parse()
        self.dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        self.triplets = {
            (0, -1): {(-1, -1), (0, -1), (1, -1)},
            (0, 1): {(-1, 1), (0, 1), (1, 1)},
            (-1, 0): {(-1, -1), (-1, 0), (-1, 1)},
            (1, 0): {(1, -1), (1, 0), (1, 1)}
        }
        
    def parse(self):
        res = set()
        lines = open(self.filename).read().split("\n")
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if lines[y][x] == "#":
                    res.add((x, y))          
        return res
                
        
    def part1(self):
        for _ in range(10):
            next_state = {}

            for elf in self.elves:
                if not any(p in self.elves for p in adjacent8(elf[0], elf[1])):
                    next_state[elf] = elf
                
            for (x, y) in self.elves:
                
                if (x, y) in next_state:
                    continue
                
                for dir in self.dirs:
                    
                    if any((x + dx, y + dy) in self.elves for (dx, dy) in self.triplets[dir]):
                        continue
                    
                    nx, ny = x + dir[0], y + dir[1]
                    
                    if (nx, ny) in next_state.values():
                        
                        # two elves wants to move to the same point
                        # stop the other elf that considers to move to the same point
                        for key, value in next_state.items():
                            if value == (nx, ny):
                                next_state[key] = key
                                break
                        break
                            
                    next_state[(x, y)] = nx, ny
                    break
                    
                if (x, y) not in next_state:
                    next_state[(x, y)] = (x, y)
                
            self.changeDirOrder()
            self.elves = {x for x in next_state.values()}
         
            
        minX, minY, maxX, maxY = self.getMinMax()
        return (maxY - minY + 1) * (maxX - minX + 1) - len(self.elves)
        
        
            
         
    def printElves(self):
        minX, minY, maxX, maxY = self.getMinMax()
        s = ""
        for y in range(minY, maxY + 1):
            for x in range(minX, maxX + 1):
                if (x, y) in self.elves:
                    s += "#"
                else:
                    s += "."
            s += "\n"
        print(s)
        
    def getMinMax(self):
        minX = min(self.elves, key=lambda e: e[0])[0]
        minY = min(self.elves, key=lambda e: e[1])[1]
        maxX = max(self.elves, key=lambda e: e[0])[0]
        maxY = max(self.elves, key=lambda e: e[1])[1]
        return minX, minY, maxX, maxY
           
    def changeDirOrder(self):
        self.dirs.append(self.dirs.pop(0))
                
    def part2(self):
        round = 10 #part 1 runs 10 rounds
        while True:
            round += 1
            next_state = {}

            c = 0
            for elf in self.elves:
                if not any(p in self.elves for p in adjacent8(elf[0], elf[1])):
                    next_state[elf] = elf
                    c+= 1
            
            if c == len(self.elves):
                return round
                
            for (x, y) in self.elves:
                
                if (x, y) in next_state:
                    continue
                
                for dir in self.dirs:
                    
                    if any((x + dx, y + dy) in self.elves for (dx, dy) in self.triplets[dir]):
                        continue
                    
                    nx, ny = x + dir[0], y + dir[1]
                    
                    if (nx, ny) in next_state.values():
                        
                        # two elves wants to move to the same point
                        # stop the other elf that considers to move to the same point
                        for key, value in next_state.items():
                            if value == (nx, ny):
                                next_state[key] = key
                                break
                        break
                            
                    next_state[(x, y)] = nx, ny
                    break
                    
                if (x, y) not in next_state:
                    next_state[(x, y)] = (x, y)
                
            self.changeDirOrder()
            self.elves = {x for x in next_state.values()}
            
            
            
    
    
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