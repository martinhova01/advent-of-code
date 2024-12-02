import time

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [line.split(" ") for line in open(self.filename).read().rstrip().split("\n")]
        
    def safe(self, line):
        return self.is_inc(line) or self.is_inc(list(reversed(line)))
        
    def is_inc(self, line):
        for i in range(len(line) - 1):
            start, end = int(line[i]), int(line[i + 1])
            if start < end + 1 or start > end + 3:
                return False
        return True
        
    def part1(self):
        
        res = 0
        for line in self.data:
            if self.safe(line):
                res += 1
        return res
    
    def part2(self):
        res = 0
        for line in self.data:
            if self.safe(line):
                res += 1
                continue
            for i in range(len(line)):
                new_line = list(line)
                del new_line[i]
                
                if self.safe(new_line):
                    res += 1
                    break
        return res
    
    
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