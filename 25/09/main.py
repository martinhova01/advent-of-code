import time
import itertools
import functools
from collections import Counter, defaultdict, deque
import networkx as nx
from tqdm import tqdm
import numpy as np
import re
import copy
from functools import cache
from matplotlib.path import Path

import sys
sys.path.append("../..")
from utils import adjacent4, adjacent8, directions4, directions8, manhattanDist

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [tuple(map(int, line.split(","))) for line in open(self.filename).read().rstrip().split("\n")]
        
    def part1(self):
        best = 0
        for i in range(len(self.data)):
            for j in range(i + i, len(self.data)):
                a = self.data[i]
                b = self.data[j]
                area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
                best = max(best, area)
            
        return best
    
    def part2(self):
        polygon = Path(self.data)
        print(polygon.contains_point(self.data[0], radius=1e-9))
        areas = {}
        
        for i in range(len(self.data)):
            for j in range(i + 1, len(self.data)):
                a = self.data[i]
                b = self.data[j]
                area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
                areas[(a, b)] = area
        
        # print(areas)
        
        
        for (a, b), value in sorted(areas.items(), key=lambda x : x[1], reverse=True):
            (x1, y1), (x2, y2) = a, b
            print(a, b, value)
            
            points = []
            for x in range(min(x1, x2), max(x1, x2) + 1):
                points.append((x, y1))
                points.append((x, y2))
            for y in range(min(y1, y2), max(y1, y2) + 1):
                points.append((x1, y))
                points.append((x2, y))
            
            if all(polygon.contains_points(points, radius=1e-9)):
                return value
        
    
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}\n")
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}") # not 4601733120
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()