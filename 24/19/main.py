import time
from functools import cache

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read().rstrip()
        patterns, designs = self.data.split("\n\n")
        self.patterns = patterns.split(", ")
        self.designs = designs.split("\n")
        
    def matches(self, design: str):
        if not design:
            return True
        for pattern in self.patterns:
            if design.startswith(pattern):
                ret = self.matches(design[len(pattern):])
                if ret:
                    return True
        return False
    
    @cache
    def num_matches(self, design: str):
        if not design:
            return 1
        s = 0
        for pattern in self.patterns:
            if design.startswith(pattern):
                s += self.num_matches(design[len(pattern):])
        return s
                
        
    def part1(self):
        return sum(1 if self.matches(design) else 0 for design in self.designs)
    
    def part2(self):
        return sum(self.num_matches(design) for design in self.designs)
    
    
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