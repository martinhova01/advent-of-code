import time
from collections import deque

import sys
sys.path.append("../..")
from utils import adjacent4

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [line for line in open(self.filename).read().rstrip().split("\n")]
        self.R = len(self.data)
        self.C = len(self.data[0])
    
    def bfs(self, regions, start_x, start_y, label):
        visited = set()
        q = deque([(start_x, start_y)])
        while q:
            x, y = q.popleft()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            
            for nx, ny in adjacent4(x, y):
                if (nx, ny) not in regions:
                    continue
                if regions[(nx, ny)] != label:
                    continue
        
                q.append((nx, ny))
                
        return visited
        
        
    def part1(self):
        regions = {}
        for y in range(self.R):
            for x in range(self.C):
                regions[(x, y)] = self.data[y][x]
        
        done = set()
        s = 0
        for(x, y), label in regions.items():
            if (x, y) in done:
                continue
            visited = self.bfs(regions, x, y, label)
            done = done.union(visited)
            area = len(visited)
            
            neighbors = 0
            for (x, y) in visited:
                for nx, ny in adjacent4(x, y):
                    if (nx, ny) not in regions:
                        continue
                    if regions[(nx, ny)] != label:
                        continue
                    neighbors += 1
            
            s += area * ((4 * area) - neighbors)
        
        return s
    
    def find_sides(self, regions, visited, label):
        sides = {}
        directions = {"UP": (0, -1), "DOWN": (0, 1), "LEFT": (-1, 0), "RIGHT": (1, 0)}
        for dir, (dx, dy) in directions.items():
            sides[dir] = set()
            for (x, y) in visited:
                if (x + dx, y + dy) not in regions:
                    sides[dir].add((x, y))
                elif regions[(x + dx, y + dy)] != label:
                    sides[dir].add((x, y))
        
        num_sides = 0
        for side, points in sides.items():
            num_sides += len(points)
            
            # consecutive points only count as one side
            for x, y in points:
                if side in ("UP", "DOWN"):
                    if (x + 1, y) in points:
                        num_sides -= 1
                else:
                    if (x, y + 1) in points:
                        num_sides -= 1
        
        return num_sides
            
    
    def part2(self):
        regions = {}
        for y in range(self.R):
            for x in range(self.C):
                regions[(y, x)] = self.data[y][x]
        
        done = set()
        s = 0
        for (x, y), label in regions.items():
            if (x, y) in done:
                continue
            visited = self.bfs(regions, x, y, label)
            area = len(visited)
            done = done.union(visited)
            
            sides = self.find_sides(regions, visited, label)
            s += area * sides
            
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