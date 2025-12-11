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

import sys
sys.path.append("../..")
from utils import adjacent4, adjacent8, directions4, directions8, manhattanDist

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read().rstrip().split("\n")
        
    def part1(self):
        G = nx.DiGraph()
        for line in self.data:
            # print(line)
            start, ends = line.split(": ")
            for end in ends.split(" "):
                G.add_edge(start, end)
                
        return len(list(nx.all_simple_paths(G, "you", "out")))
        
        print(G)
    
    def part2(self):
        G = nx.DiGraph()
        for line in self.data:
            # print(line)
            start, ends = line.split(": ")
            for end in ends.split(" "):
                G.add_edge(start, end)
                
        paths = nx.all_simple_paths(G, "svr", "out")
        # print(len(paths))
        
        s = 0
        for path in paths:
            print(path)
            if "dac" in path and "fft" in path:
                s += 1
        
        return s
    
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("---TEST---")
    # print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}\n")
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()