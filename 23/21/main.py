import time
from tqdm import tqdm
from sympy import symbols, Eq, solve

import sys
sys.path.append("../..")
from utils import directions4

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [list(line) for line in open(self.filename).read().split("\n")]
        
    
    def run(self, steps):
        points = set()
        points.add((self.findStartPos(), (0, 0))) #{((x, y), (map_offset_x, map_offset_y))}
                    
        for _ in tqdm(range(steps)):
            new_points = set()
            for (x, y), (offset_x, offset_y) in points:
                for dx, dy in directions4():
                    _x, _y, off_x, off_y = x + dx, y + dy, offset_x, offset_y
                    if _x < 0:
                        off_x -= 1
                    if _x >= len(self.data[0]):
                        off_x += 1
                    if _y < 0:
                        off_y -= 1
                    if _y >= len(self.data):
                        off_y += 1
                    
                    _x = _x % len(self.data[0])
                    _y = _y % len(self.data)
                        
                    if self.data[_y][_x] == "#":
                        continue
                    new_points.add(((_x, _y), (off_x, off_y)))
            points = new_points
        return len(points)
        
    def part1(self):
        points = set()
        points.add(self.findStartPos())
                    
        for _ in range(64):
            new_points = set()
            for (x, y) in points:
                for dx, dy in directions4():
                    _x, _y = x + dx, y + dy
                    if _x < 0 or _x >= len(self.data[0]) or _y < 0 or _y >= len(self.data):
                        continue  
                    if self.data[_y][_x] == "#":
                        continue
                    new_points.add((_x, _y))
            points = new_points
        return len(points)      
    
    def print_plots(self, points):
        res = ""
        for y in range(len(self.data)):
            for x in range(len(self.data[0])):
                if (x, y) in points:
                    res += "0"
                else:
                    res += self.data[y][x]
            res += "\n"
        print(res)
                    
    
    def findStartPos(self):
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                if self.data[y][x] == "S":
                    return (x, y)
            
    def part2(self):
        a, b, c = symbols("a b c")
        x1, y1 = 65, self.run(65)
        x2, y2 = 65 + 131, self.run(65 + 131)
        x3, y3 = 65 + 131 * 2, self.run(65 + 131 * 2)
        
        eq1 = Eq(a*x1**2 + b*x1 + c, y1)
        eq2 = Eq(a*x2**2 + b*x2 + c, y2)
        eq3 = Eq(a*x3**2 + b*x3 + c, y3)
        
        solution = solve((eq1, eq2, eq3), (a, b, c))
        
        f = lambda x : solution[a] * x**2 + solution[b] * x + solution[c]
        
        return f(26501365)
        
        
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    # print(f"part 2: {s.part2()}\n")
    
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()