import time
import itertools as it
from collections import deque

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [list(line) for line in open(self.filename).read().split("\n")]
        
    def part1(self):
        return self.calculateEnergizedTiles(0, 0, (1, 0))         
                
    def calculateEnergizedTiles(self, x, y, startdir):
        visited = set()
        energized = set()
        q = deque()
        q.append(((x, y), startdir))
        while q:
            (x, y), (dx, dy) = q.popleft()
            if x < 0 or x >= len(self.data[0]) or y < 0 or y >= len(self.data):
                continue
            c = self.data[y][x]
            dirs = []
            
            if c == "|":
                energized.add((x, y))
                if (dx, dy) == (1, 0) or (dx, dy) == (-1, 0):
                    dirs.append((0, 1))
                    dirs.append((0, -1))
                else:
                    dirs.append((dx, dy))
                    
            elif c == "-":
                energized.add((x, y))
                if (dx, dy) == (0, 1) or (dx, dy) == (0, -1):
                    dirs.append((-1, 0))
                    dirs.append((1, 0))
                else:
                    dirs.append((dx, dy))
            elif c == "/":
                energized.add((x, y))
                if (dx, dy) == (1, 0):
                    dirs.append((0, -1))
                elif (dx, dy) == (-1, 0):
                    dirs.append((0, 1))
                elif (dx, dy) == (0, 1):
                    dirs.append((-1, 0))
                elif (dx, dy) == (0, -1):
                    dirs.append((1, 0))
                    
            elif c == "\\":
                energized.add((x, y))
                if (dx, dy) == (1, 0):
                    dirs.append((0, 1))
                elif (dx, dy) == (-1, 0):
                    dirs.append((0, -1))
                elif (dx, dy) == (0, 1):
                    dirs.append((1, 0))
                elif (dx, dy) == (0, -1):
                    dirs.append((-1, 0))
            else: # "."
                visited.add(((x, y), (dx, dy)))
                energized.add((x, y))
                dirs.append((dx, dy))
                
            for dx, dy in dirs:
                if ((x + dx, y + dy), (dx, dy)) in visited:
                    continue
                q.append(((x + dx, y + dy), (dx, dy)))
                
        return len(energized)   
        
    
    def part2(self):
        maximum = 0
        for x, y in it.product(range(len(self.data)), range(len(self.data[0]))):
            if y == 0:
                maximum = max(maximum, self.calculateEnergizedTiles(x, y, (0, 1)))
            if y == len(self.data) - 1:
                maximum = max(maximum, self.calculateEnergizedTiles(x, y, (0, -1)))
            if x == 0:
                maximum = max(maximum, self.calculateEnergizedTiles(x, y, (1, 0)))
            if x == len(self.data[y]) - 1:
                maximum = max(maximum, self.calculateEnergizedTiles(x, y, (-1, 0)))
        return maximum
    
    
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