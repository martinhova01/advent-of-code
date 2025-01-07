import time
from collections import defaultdict, deque

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read().rstrip()
        self.parse()
        
    def parse(self):
        self.G = defaultdict(list)
        for line in self.data.split("\n"):
            u, v = line.split("-")
            self.G[u].append(v)
            self.G[v].append(u)
            
        
    def part1(self):
        triplets = set()
        for start_node in self.G.keys():
            q = deque([(start_node, 0, {start_node})])
            while q:
                u, steps, visited = q.popleft()
                
                if steps == 2:
                    if start_node in self.G[u]:
                        triplets.add(tuple(sorted(visited)))
                    continue
                
                for v in self.G[u]:
                    q.append((v, steps + 1, visited.union({v})))
                    
        return sum((1 if any(u.startswith("t") for u in triplet) else 0) for triplet in triplets)
                
    
    def part2(self):
        best = set()
        for start_node in self.G.keys():
            q = deque({start_node})
            visited = {start_node}
            while q:
                u = q.popleft()
                
                for v in self.G[u]:
                    if all(x in self.G[v] for x in visited):
                        visited.add(v)
                        q.append(v)
            
            if len(visited) > len(best):
                best = set(visited)
        
        return ",".join(sorted(best))
            
            
    
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