import sys
import time
from collections import deque
import networkx as nx

sys.path.append("../..")
from utils import directions4

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [list(line) for line in open(self.filename).read().split("\n")]
        
        #create a graph used in part2
    def create_graph(self):
        g = nx.Graph()
        for y in range(len(self.data)):
            for x in range(len(self.data[0])):
                if self.data[y][x] == "#":
                    continue
                for (dx, dy) in directions4():
                    _x, _y = x + dx, y + dy
                    if _x < 0 or _x >= len(self.data[0]) or _y < 0 or _y >= len(self.data):
                        continue
                    if self.data[_y][_x] != "#":
                        g.add_edge((x, y), (_x, _y))       
        return g
    
        #simpify the graph for part2 by only keeping nodes with degree > 2 (crossings) and edges between them.
    def simplify_graph(self, g):
        simplified_g = nx.Graph()
        startNode = self.findStartPos()
        endNode = self.findEndPos()
        for node in g.nodes():
            if nx.degree(g, node) > 2 or node == startNode:
                
                for (u, v) in nx.edges(g, node):
                    end, length = self.bfs(g, v, {u}, endNode, startNode)
                    simplified_g.add_edge(node, end, w=length)
                    
        return simplified_g
    
    def bfs(self, g, start, visited, endNode, startNode):
        q = deque()
        q.append(start)
        while q:
            node = q.popleft()
            visited.add(node)
            for (u, v) in nx.edges(g, node):
                if v in visited:
                    continue
                if nx.degree(g, v) > 2 or v == endNode or v == startNode:
                    return v, len(visited)
                q.append(v)
    
        #returns a DAG for part1
    def create_graph_bfs(self):
        g = nx.DiGraph()
        start = self.findStartPos()
        end = self.findEndPos()
        q = deque()
        q.append(start)
        visited = set()
        while q:
            x, y = q.popleft()
            if (x, y) == end:
                continue
            visited.add((x, y))
            if self.data[y][x] == ">":
                g.add_edge((x, y), (x + 1, y), w=-1)
                q.append((x + 1, y))
            if self.data[y][x] == "<":
                g.add_edge((x, y), (x - 1, y), w=-1)
                q.append((x - 1, y))
            if self.data[y][x] == "^":
                g.add_edge((x, y), (x, y - 1), w=-1)
                q.append((x, y - 1))
            if self.data[y][x] == "v":
                g.add_edge((x, y), (x, y + 1), w=-1)
                q.append((x, y + 1))
            
            
            if self.data[y][x] == ".":
                for (dx, dy) in directions4():
                    _x, _y = x + dx, y + dy
                    if _x < 0 or _x >= len(self.data[0]) or _y < 0 or _y >= len(self.data):
                        continue
                    if (_x, _y) in visited:
                        continue
                    
                    if (dx, dy) == (1, 0) and (self.data[_y][_x] == "." or self.data[_y][_x] == ">"):
                        g.add_edge((x, y), (_x, _y), w=-1)
                        q.append((_x, _y))
                    if (dx, dy) == (-1, 0) and (self.data[_y][_x] == "." or self.data[_y][_x] == "<"):
                        g.add_edge((x, y), (_x, _y), w=-1)
                        q.append((_x, _y))
                    if (dx, dy) == (0, 1) and (self.data[_y][_x] == "." or self.data[_y][_x] == "v"):
                        g.add_edge((x, y), (_x, _y), w=-1)
                        q.append((_x, _y))
                    if (dx, dy) == (0, -1) and (self.data[_y][_x] == "." or self.data[_y][_x] == "^"):
                        g.add_edge((x, y), (_x, _y), w=-1)
                        q.append((_x, _y))  
        return g
            
    
    def findStartPos(self):
        for x in range(len(self.data[0])):
            if self.data[0][x] == ".":
                return (x, 0)
    
    
    def findEndPos(self):
        for x in range(len(self.data[0])):
            if self.data[len(self.data) - 1][x] == ".":
                return (x, len(self.data) - 1)
            
            
    def find_longest_path(self, g, current, prev, end, visited):
        if current == end:
            return nx.path_weight(g, visited, weight="w")
        
        path_lengths = []
        for u, v in nx.edges(g, current):
            path = list(visited)
            if v in path:
                continue
            path.append(v)
            path_length = self.find_longest_path(g, v, u, end, path)
            path_lengths.append(path_length)
                
        if not path_lengths:
            return 0
        return max(path_lengths)
                   
        #We can create a DAG. Hence the longest path is the same as the shortest path when all edges has weight -1.
    def part1(self):
        g = self.create_graph_bfs()
        start = self.findStartPos()
        end = self.findEndPos()
        return nx.shortest_path_length(g, start, end, weight="w", method="bellman-ford") * -1
    
    def part2(self):
        g = self.create_graph()
        g = self.simplify_graph(g)
        start = self.findStartPos()
        end = self.findEndPos()
        return self.find_longest_path(g, start, None, end, [start])
    
            #possible solution, but slower
        # paths = list(nx.shortest_simple_paths(g, start, end, weight="w"))
        # lengths = [nx.path_weight(g, path, weight="w") for path in paths]
        # return nx.path_weight(g, paths[-1], weight="w")
    
    
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