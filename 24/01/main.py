import time

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read().strip().split("\n")
        
    def part1(self):
        first, second = [], []
        for line in self.data:
            start, stop = line.split("   ")
            first.append(int(start))
            second.append(int(stop))
        
        sorted_first = sorted(first)
        sorted_second = sorted(second)
        
        s = 0
        for i in range(len(sorted_first)):
            s += abs(sorted_first[i] - sorted_second[i])
        return s
            
    
    def part2(self):
        first, second = [], []
        for line in self.data:
            start, stop = line.split("   ")
            first.append(start)
            second.append(stop)
        
        s = 0
        for c in first:
            local_s = 0
            for c2 in second:
               if c == c2:
                   local_s += 1
            s += int(c) * local_s
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