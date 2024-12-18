import time
from collections import deque
import re

import sys
sys.path.append("../..")
from utils import adjacent4

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read().rstrip()
        self.N = 6 if self.test else 70
        
    def part1(self):
        length = 12 if self.test else 1024
        bytes = {(tuple(map(int, line.split(",")))) for line in self.data.split("\n")[:length]}
        return self.bfs(bytes)
                
    
    def bfs(self, bytes):
        goal = (6, 6) if self.test else (70, 70)
        q = deque([(0, 0, 0)])
        visited = set()
        while q:
            x, y, steps = q.popleft()
            if (x, y) == goal:
                return steps
            if (x, y) in visited:
                continue
            visited.add((x, y))
            
            for _nx, ny in adjacent4(x, y):
                if _nx < 0 or _nx > self.N or ny < 0 or ny > self.N:
                    continue
                if (_nx, ny) in bytes:
                    continue
                q.append((_nx, ny, steps + 1))
        return -1
        
    def part2(self):
        bytes = set()
        for line in self.data.split("\n"):
            x, y = [int(x) for x in re.findall(r"\d+", line)]
            bytes.add((x, y))
            if self.bfs(bytes) == -1:
                return f"{x},{y}"
    
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