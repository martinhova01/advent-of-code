import time
from tqdm import tqdm

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.rocks = [
            {(0, 0), (1, 0), (2, 0), (3, 0)}, # -
            {(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)}, # +
            {(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)}, # L
            {(0, 0), (0, 1), (0, 2), (0, 3)}, # I
            {(0, 0), (1, 0), (0, 1), (1, 1)}, # square
        ]
        self.jets = open(self.filename).read().strip()
        self.chamber = set()
        
    def draw(self, y_range: int):
        r = ""
        for y in range(y_range, -1, -1):
            for x in range(7):
                if (x, y) in self.chamber:
                    r += "#"
                else:
                    r += "."
            r += "\n"   
        print(r)
        
            
        
        
    def sim(self, times):
        
        jetpointer = 0
        max_y = 0
        
        for i in range(times):
            
            piece = self.rocks[i % 5]
        
            x = 2
            if not self.chamber:
                y = 3
            else:
                y = max_y + 4
            
            while True:
                    #move horisontally
                nx = x - 1 if self.jets[jetpointer % len(self.jets)] == "<" else x + 1
                if all((nx + dx, y + dy) not in self.chamber and nx + dx > -1 and nx + dx < 7 for dx, dy in piece):
                    x = nx
                jetpointer += 1
                
                    # move down
                if y == 0:
                    break
                if not all((x + dx, y + dy - 1) not in self.chamber for dx, dy in piece):
                    break
                y -= 1
                
            for dx, dy in piece:
                self.chamber.add((x + dx, y + dy))
                max_y = max(max_y, y + dy)
                
        return max_y
                
               
        
    def part1(self):
        return self.sim(2022)
    
    def part2(self):
        pass
    
    
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