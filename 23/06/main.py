from functools import reduce
import time

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [self.parseLine(line) for line in open(self.filename).read().split("\n")]
        
    def parseLine(self, line):
        return [int(x) for x in line.split(":")[1].split()]
        
    def part1(self):
        margins = []
        for i in range(len(self.data[1])):
            c = 0
            for j in range(self.data[0][i]):
                d  = j * (self.data[0][i] - j)
                if d > self.data[1][i]:
                    c += 1
            margins.append(c)
        return reduce(lambda x, y: x * y, margins)
                     
    
    def part2(self):
        time = ""
        dist = ""
        for i in range(len(self.data[0])):
            time += str(self.data[0][i])
            dist += str(self.data[1][i])
            
        time, dist = int(time), int(dist)
        c = 0
        for j in range(time):
            d  = j * (time - j)
            if d > dist:
                c += 1   
        return c
    
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