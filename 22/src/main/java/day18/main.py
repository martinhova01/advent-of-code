import time
from collections import deque


class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = set(eval(f"({line})") for line in open(self.filename).read().split("\n"))
        self.min_x, self.min_y, self.min_z = min(x[0] for x in self.data), min(x[1] for x in self.data), min(x[2] for x in self.data)
        self.max_x, self.max_y, self.max_z = max(x[0] for x in self.data), max(x[1] for x in self.data), max(x[2] for x in self.data)
        self.dirs = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
        
    def part1(self):
        return self.count_area()
    
    def part2(self):
        
        for x in range(self.min_x, self.max_x + 1):
            for y in range(self.min_y, self.max_y + 1):
                for z in range(self.min_z, self.max_z + 1):
                    if (x, y, z) in self.data:
                        continue
                    self.bfs(x, y, z)
        
        return self.count_area()
        
        
    def count_area(self):
        s = 0
        for (x, y, z) in self.data:
            for dir in self.dirs:
               if (x + dir[0], y + dir[1], z + dir[2]) not in self.data:
                   s += 1   
        return s
    
    #find the interior pockets using bfs and add them to the set of cubes.
    def bfs(self, start_x, start_y, start_z):
        q = deque()
        q.append((start_x, start_y, start_z))
        visited = set()
        while q:
            (x, y, z) = q.popleft()
            if self.is_out_of_bounds(x, y, z):
                return
            visited.add((x, y, z))
            
            for dir in self.dirs:
                _x, _y, _z = x + dir[0], y + dir[1], z + dir[2]
                if (_x, _y, _z) in self.data or (_x, _y, _z) in visited:
                    continue
                visited.add((_x, _y, _z))
                q.append((_x, _y, _z))
                
        for (x, y, z) in visited:
            self.data.add((x, y, z))
                   
                
    def is_out_of_bounds(self, x, y, z):
        return (
            x < self.min_x or x > self.max_x 
            or y < self.min_y or y > self.max_y
            or z < self.min_z or z > self.max_z
        )
    
    
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