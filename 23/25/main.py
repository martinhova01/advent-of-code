import time
import networkx as nx


class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        
    def create_graph(self):
        g = nx.Graph()
        for line in open(self.filename).read().split("\n"):
            u, vs = line.split(": ")
            vs = vs.split(" ")
            for v in vs:
                g.add_edge(u, v, c=1)
        return g
        
    def part1(self):
        g = self.create_graph()
        for s in g.nodes():
            for t in g.nodes():
                if s == t:
                    continue
                if nx.maximum_flow_value(g, s, t, capacity="c") == 3:
                    partition = nx.minimum_cut(g, s, t, capacity="c")[1]
                    return len(partition[0]) * len(partition[1])
                    
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()