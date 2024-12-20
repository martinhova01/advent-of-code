import time
from collections import deque
import networkx as nx
from tqdm import tqdm

import sys
sys.path.append("../..")
from utils import adjacent4

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [list(x) for x in open(self.filename).read().rstrip().split("\n")]
        self.R = len(self.data)
        self.C = len(self.data[0])
        
        
    def part1(self):
        G = nx.Graph()
        start, end = None, None
        for y in range(1, self.R - 1):
            for x in range(1, self.C - 1):
                if self.data[y][x] == "#":
                    continue
                if self.data[y][x] == "S":
                    start = (x, y)
                
                if self.data[y][x] == "E":
                    end = (x, y)
                
                for _nx, ny in adjacent4(x, y):
                    if self.data[ny][_nx] in ".SE":
                        G.add_edge((x, y), (_nx, ny))
                        
        # try adding cheats at all possible positions
        original_shortest_path = nx.shortest_path_length(G, start, end)
        cheats = []
        for y in range(1, self.R - 1):
            for x in range(1, self.C - 1):
                if self.data[y][x] == "#":
                    continue
                
                for dx, dy in ((1, 0), (0, 1)): # right, down
                    if x + 2*dx < 0 or x + 2*dx >= self.C or y + 2*dy < 0 or y + 2*dy >= self.R:
                        continue
                    
                    if self.data[y + 2*dy][x + 2*dx] != "#":
                        new_edges = []
                        for i in range(2):
                            e = ((x + i*dx, y + i*dy), (x + (i+1)*dx, y + (i+1)*dy))
                            if e in G.edges:
                                continue
                            G.add_edge(*e)
                            new_edges.append(e)
                        
                        new_shortest = nx.shortest_path_length(G, start, end)
                        if new_shortest <= original_shortest_path - (2 if self.test else 100):
                            cheats.append((x, y, original_shortest_path - new_shortest))
                        G.remove_edges_from(new_edges)
              
        return len(cheats) 
                        
                        
    def find_original_shortest_paths(self, end):
        q = deque([(*end, 0)])
        visited = set()
        result = {}
        while q:
            x, y, steps = q.popleft()
            result[(x, y)] = steps
            if (x, y) in visited:
                continue
            visited.add((x, y))
            
            for _nx, ny in adjacent4(x, y):
                if _nx < 0 or _nx >= self.C or ny < 0 or ny >= self.R:
                    continue
                if self.data[ny][_nx] == "#":
                    continue
                q.append((_nx, ny, steps + 1))
        
        return result

    def cheat_bfs(self, start_x, start_y, original_shortest_paths):
        q = deque([(start_x, start_y, 20)]) #(x, y, cheat_steps)
        visited = set()
        result = set()
        
        while q:
            x, y, cheat_steps = q.popleft()
            if (x, y) in visited or cheat_steps == -1:
                continue
            visited.add((x, y))
            
            if self.data[y][x] in ".E":
                if (x, y) not in original_shortest_paths:
                    # ended up at an ilegal position
                    continue
                
                saved = original_shortest_paths[(start_x, start_y)] - original_shortest_paths[(x, y)] - (20 - cheat_steps)
                if saved >= (50 if self.test else 100):
                    result.add(((start_x, start_y), (x, y)))
            
            for _nx, ny in adjacent4(x, y):
                if _nx < 0 or _nx >= self.C or ny < 0 or ny >= self.R:
                    continue
                q.append((_nx, ny, cheat_steps - 1))
                
        return result
                        
    
    def find_cheats(self, original_shortest_paths):
        result = set()
        for y in tqdm(range(1, self.R - 1)):
            for x in range(1, self.C - 1):
                if self.data[y][x] == "#":
                    continue
                result = result.union(self.cheat_bfs(x, y, original_shortest_paths))
        return result
    
    def part2(self):
        end = None
        for y in range(1, self.R - 1):
            for x in range(1, self.C - 1):
                if self.data[y][x] == "E":
                    end = (x, y)
        
        original_shortest_paths = self.find_original_shortest_paths(end)
        cheats = self.find_cheats(original_shortest_paths)
        return len(cheats)
    
    
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