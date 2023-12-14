import time
import numpy as np
from tqdm import tqdm

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = np.array([[x for x in line] for line in open(self.filename).read().split("\n")])
        
    def part1(self):
        self.moveAllNorth()    
        return self.calculateLoad()   
    
    
    def moveAllNorth(self):
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                if self.data[y][x] == "O":
                    self.moveNorth(x, y)
    
      
    def moveNorth(self, x, y):
        if y - 1 < 0:
                return   
        i = 1
        while self.data[y - i][x] == ".":
            if y - i < 0:
                return      
            self.data[y - i][x] = "O"
            self.data[y - i + 1][x] = "."
            i += 1
            
    def PerformCycle(self):
        for _ in range(4):
            self.moveAllNorth()
            self.data = np.rot90(self.data, k=-1)
            
            
    def calculateLoad(self):
        s = 0
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                if self.data[y][x] == "O":
                    s += len(self.data) - y        
        return s
    
    
    def toString(self):
        s = ""
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                s += self.data[y][x] 
        return s
                
    
    def part2(self):
        states = []
        stop = 0
        states.append(self.toString())
        for cycle in tqdm(range(1, 1000000001)):
            self.PerformCycle()
            if self.toString() in states:
                stop = cycle
                break
            states.append(self.toString())
            
        start = 0
        for i in range(len(states)):
            if states[i] == self.toString():
                start = i
                break
        lengthOfCycle = stop - start
        left = (1000000000 - start) % lengthOfCycle
        
        for _ in range(left):
            self.PerformCycle()
            
        return self.calculateLoad()
    
    
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