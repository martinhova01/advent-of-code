import time
# import itertools
# from collections import Counter, defaultdict, deque
import networkx as nx
# from tqdm import tqdm
# import numpy as np
import re
# import matplotlib.pyplot as plt


class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.mapping, self.flow_rates = self.parse()
        self.g: nx.Graph = self.create_graph()
        self.APSP = dict(nx.all_pairs_shortest_path(self.g))
        self.memo = {}
        # self.preassure_memo = {}
        self.valve_masks = {valve: 1 << i for i, valve in enumerate(self.flow_rates)}
        # print(self.valve_masks)
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
            
            
    def get_preassure(self, bitmask_open_valves: int):
        s = 0
        for v in self.flow_rates.keys():
            if bitmask_open_valves & self.valve_masks[v]:
                s += self.flow_rates[v]
        return s
            
            
    def find_max_preassure(self, valve: str, time: int, bitmask_open_valves: int):
        max_value = 0
        for end_valve, path in self.APSP[valve].items():
            if self.flow_rates[end_valve] == 0:
                continue
            if end_valve == valve:
                continue
            
            if self.valve_masks[end_valve] & bitmask_open_valves:
                continue
            
            if time - len(path) <= 0:
                continue
            
            preassure = self.get_preassure(bitmask_open_valves) * len(path)
            
            new_open_valves = bitmask_open_valves | self.valve_masks[end_valve]
            
            new_time = time - len(path)
            
            hashable = (end_valve, new_time, new_open_valves)
            
            if hashable in self.memo:
                val = self.memo[hashable]
            else:
                val = self.find_max_preassure(end_valve, new_time, new_open_valves)
                self.memo[hashable] = val
                
            if preassure + val > max_value:
                max_value = preassure + val
        
        if max_value == 0:
            return self.get_preassure(bitmask_open_valves) * time
        return max_value
            
    def part1(self):
        return self.find_max_preassure("AA", 30, 0, )
        
    
    def part2(self):
        pass
    
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}\n")
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}") #1762 too low
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()