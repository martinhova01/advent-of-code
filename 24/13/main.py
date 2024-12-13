import time
import numpy as np
import re

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read().rstrip()
        
    def parse(self, part):
        machines = []
        for section in self.data.split("\n\n"):
            matches = [int(x) for x in re.findall(r"\d+", section)]
            A = np.array([[matches[0], matches[2]], [matches[1], matches[3]]])
            B = np.array([x + 0 if part == 1 else x + 10000000000000 for x in matches[4:]])
            machines.append((A, B))
        return machines
            
        
    def part1(self):
        machines = self.parse(1)
        s = 0
        for machine in machines:
            A, B = machine
            a, b = np.linalg.solve(A, B)
            if a > 100 or b > 100:
                continue
            if np.isclose(0, abs(a - np.round(a))) and np.isclose(0, abs(b - np.round(b))):
                s += 3 * np.round(a) + np.round(b)
        return s
    
    def part2(self):
        machines = self.parse(2)
        s = 0
        for machine in machines:
            A, B = machine
            a, b = np.linalg.solve(A, B)
            if np.isclose(0, abs(a - np.round(a)), atol=1e-2) and np.isclose(0, abs(b - np.round(b)), atol=1e-2):
                s += 3 * np.round(a) + np.round(b)
        return s
    
    
    
def main():
    print()
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