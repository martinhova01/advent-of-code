import time
import itertools

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read().rstrip().split("\n")
        
    def is_valid(self, target, values, part1):
        operators = "*+" if part1 else "*+|"
        for ops in itertools.product(operators, repeat=len(values) - 1):
            res = values[0]
            for i in range(len(ops)):
                if ops[i] == "*":
                    res *= values[i + 1]
                elif ops[i] == "+":
                    res += values[i + 1]
                elif ops[i] == "|":
                    res = int(str(res) + str(values[i + 1]))
            if res == target:
                return True
        return False

    def parse_line(self, line: str):
        target, values = line.split(": ")
        target = int(target)
        values = list(map(int, values.split(" ")))
        return target, values
        
        
    def part1(self):
        s = 0
        for line in self.data:
            target, values = self.parse_line(line)
            if self.is_valid(target, values, True):
                s += target
        return s
            
    
    def part2(self):
        s = 0
        for line in self.data:
            target, values = self.parse_line(line)
            if self.is_valid(target, values, False):
                s += target
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