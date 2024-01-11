import time
import numpy as np
from sympy import symbols, Eq, solve

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
        coordsA = A[0][:-1]
        coordsB = B[0][:-1]
        vectorA = A[1][:-1]
        vectorB = B[1][:-1]
        a_A = vectorA[1] / vectorA[0]
        a_B = vectorB[1] / vectorB[0]
        
            #parallell
        if a_A == a_B:
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
        x, y, z, vx, vy, vz, *t = symbols("x y z vx vy vz t1 t2 t3")
        eqs = []
        for i in range(3):
            coords = self.data[i][0]
            vector = self.data[i][1]
            eqs.append(Eq(x + vx * t[i], coords[0] + vector[0] * t[i]))
            eqs.append(Eq(y + vy * t[i], coords[1] + vector[1] * t[i]))
            eqs.append(Eq(z + vz * t[i], coords[2] + vector[2] * t[i]))
            
        sol = solve(eqs)
        return sol[0][x] + sol[0][y] + sol[0][z]
    
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