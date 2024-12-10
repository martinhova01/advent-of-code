import time
from collections import deque

import sys
sys.path.append("../..")
from utils import adjacent4

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [[int(x) for x in line] for line in open(self.filename).read().rstrip().split("\n")]
        self.R = len(self.data)
        self.C = len(self.data[0])
        
    def bfs(self, start_x, start_y):
        s = 0
        q = deque()
        q.append((start_x, start_y))
        visited = set()
        while q:
            x, y = q.popleft()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            
            if self.data[y][x] == 9:
                s += 1
                continue
            
            for nx, ny in adjacent4(x, y):
                if nx < 0 or nx >= self.C or ny < 0 or ny >= self.R:
                    continue
                if self.data[ny][nx] != self.data[y][x] + 1:
                    continue
                
                q.append((nx, ny))
        return s
        
    def part1(self):
        s = 0
        R = len(self.data)
        C = len(self.data[0])
        
        for y in range(R):
            for x in range(C):
                if self.data[y][x] != 0:
                    continue
                s += self.bfs(x, y)
        return s
    
    def bfs2(self, start_x, start_y):
        s = 0
        q = deque()
        q.append((start_x, start_y, -1, -1))
        while q:
            x, y, last_x, last_y = q.popleft()
            
            if self.data[y][x] == 9:
                s += 1
                continue
            
            for nx, ny in adjacent4(x, y):
                if nx < 0 or nx >= self.C or ny < 0 or ny >= self.R:
                    continue
                if self.data[ny][nx] != self.data[y][x] + 1:
                    continue
                if (nx, ny) == (last_x, last_y):
                    continue
                
                q.append((nx, ny, x, y))
        return s
    
    def part2(self):
        s = 0
        R = len(self.data)
        C = len(self.data[0])
        
        for y in range(R):
            for x in range(C):
                if self.data[y][x] != 0:
                    continue
                s += self.bfs2(x, y)
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