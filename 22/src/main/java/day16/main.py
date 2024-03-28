import time
import itertools
from collections import Counter, defaultdict, deque
import networkx as nx
from tqdm import tqdm
import numpy as np
import re
import matplotlib.pyplot as plt

# import sys
# sys.path.append("../..")
# from utils import adjacent4, adjacent8, directions4, directions8

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.mapping, self.flow_rates = self.parse()
        self.g: nx.Graph = self.create_graph()
        self.APSP = dict(nx.all_pairs_shortest_path(self.g))
        self.memo = {}
        # print(self.flow_rates)
        # print(self.APSP)
        # nx.draw_networkx(self.g)
        # plt.show()
        
    def create_graph(self):
        g = nx.Graph()
        for startnode, endnodes in self.mapping.items():
            for endnode in endnodes:
                g.add_edge(startnode, endnode)
        return g
        
        
    def parse(self):
        flow_rates = {}
        mapping = {}
        for line in open(self.filename).read().split("\n"):
            valve, *valves = re.findall(r"([A-Z]{2})", line)
            flow = int(re.findall(r"(\d+)", line)[0])
            flow_rates[valve] = flow
            mapping[valve] = set(valves)
        return mapping, flow_rates
            
            
    def get_preassure(self, open_valves, time):
        s = 0
        for v in open_valves:
            s += self.flow_rates[v]
        return s * time
            
            
    def find_max_preassure(self, valve: str, time: int, preassure: int, open_valves: set):
        # print(valve, time, preassure, open_valves)
        values = []
        for end_valve, path in self.APSP[valve].items():
            # print(end_valve)
            if end_valve == valve:
                continue
            
            if end_valve in open_valves:
                continue
            
            if time + len(path) >= 30:
                continue
            
            new_open_valves = set(open_valves)
            new_open_valves.add(end_valve)
            # print(new_open_valves)
            
            hashable = (end_valve, time + len(path), preassure + self.get_preassure(open_valves, len(path)), tuple(sorted(list(new_open_valves))))
            # print(hashable)
            if hashable in self.memo:
                # print(time)
                # print(self.memo)
                # print(hashable)
                # print("found")
                # if not self.test:
                #     print("found")
                val = self.memo[hashable]
            else:
                val = self.find_max_preassure(end_valve, time + len(path), preassure + self.get_preassure(open_valves, len(path)), new_open_valves)
                self.memo[hashable] = val
            
            values.append(val)
        
        if not values:
            return preassure + self.get_preassure(open_valves, 30 - time)
        return max(values)
            
    def part1(self):
        open_valves = set()
        open_valves.add("AA")
        return self.find_max_preassure("AA", 0, 0, open_valves)
    
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