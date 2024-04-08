import time
import networkx as nx
import re


class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.mapping, self.flow_rates = self.parse()
        self.g: nx.Graph = self.create_graph()
        self.APSP = dict(nx.all_pairs_shortest_path(self.g))
        self.valve_masks = {valve: 1 << i for i, valve in enumerate(self.flow_rates)}
        
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
    
            
    def find_max_pressure(self, valve: str, time: int, pressure, bitmask_open_valves: int, best: dict[int, int]):
        
        best[bitmask_open_valves] = max(best.get(bitmask_open_valves, 0), pressure)
        
        for end_valve, path in self.APSP[valve].items():
            if self.flow_rates[end_valve] == 0:
                continue
            if end_valve == valve:
                continue
            
            if self.valve_masks[end_valve] & bitmask_open_valves:
                continue
            

            new_time = time - len(path)
            if new_time <= 0:
                continue
            
            new_preassure = pressure + new_time * self.flow_rates[end_valve]
            
            new_open_valves = bitmask_open_valves | self.valve_masks[end_valve]
            
            self.find_max_pressure(end_valve, new_time, new_preassure, new_open_valves, best)
            
        return best
            
    def part1(self):
        return max(self.find_max_pressure("AA", 30, 0, 0, {}).values())
        
    
    def part2(self):
        best = self.find_max_pressure("AA", 26, 0, 0, {})
        return max(
            press1 + press2
            for bitmask1, press1 in best.items()
            for bitmask2, press2 in best.items()
            if not bitmask1 & bitmask2
        )
    
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