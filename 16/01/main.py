import time

import sys
sys.path.append("../..")
from utils import manhattanDist

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read().split(", ")
        
    def part1(self):
        x, y, = 0, 0
        facing = [0, -1]
        for instruction in self.data:
            _dir, count = instruction[0], int(instruction[1:])
            if _dir == "R":
                facing = [facing[1], -facing[0]]
            else:
                facing = [-facing[1], facing[0]]
            x += facing[0] * count
            y += facing[1] * count
        
        return manhattanDist(0, 0, x, y)
                
    
    def part2(self):
        visited = set((0, 0))
        x, y, = 0, 0
        facing = [0, -1]
        for instruction in self.data:
            _dir, count = instruction[0], int(instruction[1:])
            if _dir == "R":
                facing = [facing[1], -facing[0]]
            else:
                facing = [-facing[1], facing[0]]
            for _ in range(count):
                x += facing[0]
                y += facing[1]
                if (x, y) in visited:
                    return manhattanDist(0, 0, x, y)
                visited.add((x, y))
    
    
def main():
    start = time.perf_counter()
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()