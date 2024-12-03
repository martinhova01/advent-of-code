import time
import re

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read().rstrip()
        
    def part1(self):
        return sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", self.data))
            
    
    def part2(self):
        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        matches = re.finditer(pattern, self.data)
        
        do = True
        last_i = 0
        s = 0
        for match in matches:
            i = match.start()
            
            if do:  
                if "don't()" in self.data[last_i : i]:
                    do = False
            else:
                if "do()" in self.data[last_i : i]:
                    do = True
                    
            if do:
                x, y = match.groups()
                s += int(x) * int(y)
            last_i = i
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