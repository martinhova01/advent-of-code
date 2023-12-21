import sys
import time
import itertools
from collections import Counter, defaultdict, deque
import networkx as nx
from tqdm import tqdm
import numpy as np
import re

sys.path.append("../..")
from utils import adjacent4, adjacent8, directions4, directions8

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [list(line) for line in open(self.filename).read().split("\n")]
        # print(self.data)
        
    def part1(self):
        steps = 0
        points = set()
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                if self.data[y][x] == "S":
                    points.add((x, y))
                    
        for i in range(64):
            new_points = set()
            for x, y in points:
                for dx, dy in directions4():
                    _x, _y = x + dx, y + dy
                    if _x < 0 or _x >= len(self.data[0]) or _y < 0 or _y >= len(self.data):
                        continue
                    if self.data[_y][_x] == "#":
                        continue
                    new_points.add((_x, _y))
                    points = new_points
                    
        return len(points)
            
    
    def part2(self):
        steps = 26501365 if not self.test else 10
        points = {}
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                if self.data[y][x] == "S":
                    points[(x, y)] = 1
                    
        for _ in tqdm(range(steps)):
            new_points = {}
            for (x, y), num in points.items():
                for dx, dy in directions4():
                    _x, _y = (x + dx) % len(self.data[0]), (y + dy) % len(self.data)
                    if self.data[_y][_x] == "#":
                        continue
                    if (_x, _y) not in new_points:
                        new_points[(_x, _y)] = 0
                    new_points[(_x, _y)] += num
                    points = new_points
                    
        print(points)
        return sum(x for x in points.values())
    
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}\n")
    
    # s = Solution()
    # print("---MAIN---")
    # print(f"part 1: {s.part1()}")
    # print(f"part 2: {s.part2()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()