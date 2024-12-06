import time
import copy

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [list(line) for line in open(self.filename).read().rstrip().split("\n")]
        self.start_x, self.start_y = self.find_start_pos()
        
    def find_start_pos(self):
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                if self.data[y][x] == "^":
                    self.data[y][x] = "."
                    return x, y
                    
    def print_path(self, visited):
        p = ""
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                c = self.data[y][x]
                if (x, y) in visited:
                    p += "X"
                else:
                    p += c
            p +="\n"
        print(p)
        
    def part1(self):
        visited = set()
        visited.add((self.start_x, self.start_y))
        dx, dy = 0, -1
        x, y = [self.start_x, self.start_y]
        
        while True:
            nx, ny = x + dx, y + dy
            
            if nx < 0 or nx >= len(self.data[0]) or ny < 0 or ny >= len(self.data):
                break
        
            if (self.data[ny][nx] == "#"):
                dx, dy = -dy, dx
                continue
            
            x, y = nx, ny
            visited.add((nx, ny))
            
        return len(visited)
    
    def valid(self, grid):
        visited = set()
        visited.add((self.start_x, self.start_y, 0, -1)) #(x, y, dir_x, dir_y)
        dx, dy = 0, -1
        x, y = self.start_x, self.start_y
        
        while True:
            if (x, y, dx, dy) in visited and len(visited) > 1:
                return True
            visited.add((x, y, dx, dy))
            
            nx, ny = x + dx, y + dy
            
            if nx < 0 or nx >= len(grid[0]) or ny < 0 or ny >= len(grid):
                return False
        
            if (grid[ny][nx] == "#"):
                dx, dy = -dy, dx
                continue
            
            x, y = nx, ny
              
    
    def part2(self):
        s = 0
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                if self.data[y][x] == "#":
                    continue
                grid = copy.deepcopy(self.data)
                grid[y][x] = "#"
                if self.valid(grid):
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