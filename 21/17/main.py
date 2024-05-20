import time
import re

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.min_x, self.max_x, self.min_y, self.max_y = [int(x) for x in re.findall(r"-?\d+", open(self.filename).read())]
        self.hits = self.find_hits()
        
    def find_hits(self):
        hits = []
        for vx in range(2 * self.max_x):
            for vy in range(2 * self.min_y, -2 * self.min_y):
                if self.is_hit(vx, vy):
                    hits.append((vx, vy))
        return hits
    
    
    def is_hit(self, vx, vy):
        x, y = 0, 0
        while True:
            x += vx
            y += vy
            vx = vx - 1 if vx > 0 else 0
            vy -= 1
            if x >= self.min_x and x <= self.max_x and y >= self.min_y and y <= self.max_y:
                return True
            if x > self.max_x or y < self.min_y:
                return False    
            
    def find_height(self, vx, vy):
        x, y = 0, 0
        max_y = y
        while True:
            x += vx
            y += vy
            vx = vx - 1 if vx > 0 else 0
            vy -= 1
            max_y = max(max_y, y)
            if x > self.max_x or y < self.min_y:
                break
        return max_y
   

    def part1(self):
        best = max(self.hits, key=lambda p: p[1])
        return self.find_height(*best)
    
    def part2(self):  
        return len(self.hits)
    
    
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