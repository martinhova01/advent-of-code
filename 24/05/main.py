import time
import networkx as nx
from collections import defaultdict

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read().rstrip()
        self.invalids = []
        self.d = defaultdict(list)
        
    def part1(self):
        rules, pages = self.data.split("\n\n")
        rules = [[int(x) for x in line.split("|")] for line in rules.split("\n")]
        for rule in rules:
            self.d[rule[0]].append(rule[1])
        s = 0
        for page in pages.split("\n"):
            page = [int(x) for x in page.split(",")]
            valid = True
            for i, num in enumerate(page):
                if num in self.d:
                    if any(page[j] in self.d[num] for j in range(i)):
                        #invalid
                        valid = False
                        self.invalids.append(page)
                        break
            if valid:
                s += page[len(page) // 2]
        
        return s
                    
                    
    def part2(self):
        s = 0
        for page in self.invalids:
            G = nx.DiGraph()
            for n1 in page:
                if n1 not in self.d:
                    continue
                for n2 in self.d[n1]:
                    if n2 not in page:
                        continue
                    G.add_edge(n1, n2)
        
            top_sort = list(nx.topological_sort(G))
            s += top_sort[len(page) // 2]
        return s
                
    
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