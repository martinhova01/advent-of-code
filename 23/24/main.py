import time
import numpy as np

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [self.parseLine(line) for line in open(self.filename).read().split("\n")]
        self.lower = 7 if test else 200000000000000
        self.upper = 27 if test else 400000000000000
        
    def parseLine(self, line):
        split = line.split(" @ ")
        coords = eval(f"({split[0]})")
        vector = eval(f"({split[1]})")
        return (coords, vector)
        
    def part1(self):
        s = 0
        for i in range(len(self.data)):
            for j in range(i + 1, len(self.data)):
                if self.check_intersection(self.data[i], self.data[j], self.lower, self.upper):
                    s += 1 
        return s
    
    def check_intersection(self, A, B, lower, upper):
        coordsA = np.array([A[0][0], A[0][1]])
        coordsB = np.array([B[0][0], B[0][1]])
        vectorA = np.array([A[1][0], A[1][1]])
        vectorB = np.array([B[1][0], B[1][1]])
        a_A = vectorA[1] / vectorA[0]
        a_B = vectorB[1] / vectorB[0]
        
            #parallell
        if np.all(vectorA / vectorB == vectorA[0] / vectorB[0]):
            return False
        
        f_A = lambda x : a_A * (x - coordsA[0]) + coordsA[1]
        
            #y1 = y2 => solve for x
        crossing_x = (-a_B * coordsB[0] + coordsB[1] + a_A * coordsA[0] - coordsA[1]) / (a_A - a_B)
        crossing_y = f_A(crossing_x)
        
        if crossing_x < lower or crossing_x > upper or crossing_y < lower or crossing_y > upper:
            return False
        
        timeA = (crossing_x - coordsA[0]) / vectorA[0]
        if timeA < 0:
            return False
        timeB = (crossing_x - coordsB[0]) / vectorB[0]
        if timeB < 0:
            return False
    
        return True
        
    
    def part2(self):
        return None
    
    
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