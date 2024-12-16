import time
from collections import deque
import networkx as nx

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [list(x) for x in open(self.filename).read().rstrip().split("\n")]
        self.G = nx.DiGraph()
        
    def find_shortest_paths(self):
        R = len(self.data)
        C = len(self.data[0])
        start_x, start_y, end_x, end_y = None, None, None, None
        for y in range(1, R - 1):
            for x in range(1, C - 1):
                if self.data[y][x] == "S":
                    start_x, start_y = x, y
                if self.data[y][x] == "E":
                    end_x, end_y = x, y
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        visited = set()
        q = deque([(start_x, start_y, 0)])
        while q:
            x, y, dir = q.popleft()
            if (x, y, dir) in visited:
                continue
            visited.add((x, y, dir))
            
            _nx, ny = x + directions[dir][0], y + directions[dir][1]
            if self.data[ny][_nx] == ".":
                self.G.add_edge((x, y, dir), (_nx, ny, dir), w=1)
                q.append((_nx, ny, dir))
            
            if self.data[ny][_nx] == "E":
                self.G.add_edge((x, y, dir), (_nx, ny, -1), w=1)
            
            self.G.add_edge((x, y, dir), (x, y, (dir + 1) % 4), w=1000)
            q.append((x, y, (dir + 1) % 4))
            self.G.add_edge((x, y, dir), (x, y, (dir - 1) % 4), w=1000)
            q.append((x, y, (dir - 1) % 4))
            
        return list(nx.all_shortest_paths(self.G, (start_x, start_y, dir), (end_x, end_y, -1), weight="w"))
        
    def part1(self):
        return nx.path_weight(self.G, self.find_shortest_paths()[0], weight="w")
        
    def part2(self):
        paths = self.find_shortest_paths()
        res = set()
        for path in paths:
            for x, y, _ in path:
                res.add((x, y))
        return len(res)
    
    
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