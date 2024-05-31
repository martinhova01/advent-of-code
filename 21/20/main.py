import time
import itertools as it

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.parse()
        
    def parse(self):
        lines = open(self.filename).read().split("\n")
        self.lookup: list = [x == "#" for x in lines[0]] 
        
        self.pixels = set()
        image_lines = lines[2:]
        for y in range(len(image_lines)):
            for x in range(len(image_lines)):
                if image_lines[y][x] == "#":
                    self.pixels.add((x, y))
        
    def apply(self, times):
        
        for time in range(times):
            new_pixels = set()
            self.lookup = [not x for x in self.lookup] # invert lookup list
        
            min_x, max_x, min_y, max_y = float("inf"), -float("inf"), float("inf"), -float("inf")
            for x, y in self.pixels:
                min_x, max_x, min_y, max_y = min(min_x, x), max(max_x, x), min(min_y, y), max(max_y, y)
            
            for y in range(min_y - 1, max_y + 2):
                for x in range(min_x - 1, max_x + 2):
                    index = ""
                    for dy, dx in it.product((-1,0,1), repeat=2):
                        if time % 2 == 0:
                            #self.pixels tracks white pixels
                            index += "1" if (x + dx, y + dy) in self.pixels else "0"
                        else:
                            #self.pixels tracks black pixels
                            index += "1" if (x + dx, y + dy) not in self.pixels else "0"
                    index = int(index, 2)
                    if self.lookup[index]:
                        new_pixels.add((x, y))
                    
            self.pixels = new_pixels
    
    def part1(self):
        self.apply(2)
        return len(self.pixels)
    
    def part2(self):
        self.parse()
        self.apply(50)
        return len(self.pixels)
    
    
def main():
    start = time.perf_counter()
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()