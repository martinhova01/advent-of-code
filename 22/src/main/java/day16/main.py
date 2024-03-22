import time
import itertools
from collections import Counter, defaultdict, deque
import networkx as nx
from tqdm import tqdm
import numpy as np
import re

# import sys
# sys.path.append("../..")
# from utils import adjacent4, adjacent8, directions4, directions8

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.mapping = {}
        self.flow_rates = {}
        self.parse()
        self.DP = {}
        print(self.mapping)
        print(self.flow_rates)
        
        
    def parse(self):
        for line in open(self.filename).read().split("\n"):
            valve, *valves = re.findall(r"([A-Z]{2})", line)
            flow = int(re.findall(r"(\d+)", line)[0])
            self.flow_rates[valve] = flow
            self.mapping[valve] = set(valves)
            
            
    def get_preassure(self, open_valves):
        s = 0
        for v in open_valves:
            s += self.flow_rates[v]
        return s
            
            
    def find_max_preassure(self, valve: str, time: int, preassure: int, open_valves: set):
        if time <= 0:
            return preassure
        vals = []
        new_time = time - 1
        if valve not in open_valves:
            new_valves = set(open_valves)
            new_valves.add(valve)
            new_pressure = preassure + time * self.flow_rates[valve]
            vals.append(self.find_max_preassure(valve, new_time, new_pressure, new_valves))
            
        for v in self.mapping[valve]:
            if v in open_valves:
                continue
            vals.append(self.find_max_preassure(v, new_time, preassure, open_valves))
            
        print(vals, time)
        if not vals:
            return preassure
        return max(vals)
            
            
        
        
    def part1(self):
        return self.find_max_preassure("AA", 30, 0, set())
    
    def part2(self):
        return None
    
    
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