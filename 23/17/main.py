import math
import sys
import time
import heapq

sys.path.append("../..")
from utils import directions4


class Node():
    def __init__(self, x, y, w, d, dir, consecutive_steps):
        self.x = x
        self.y = y
        self.w = w
        self.d = d
        self.dir = dir
        self.consecutive_steps = consecutive_steps
        
        #just pick one
    def __lt__(self, other):
        return 1


class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [[int(x) for x in line] for line in open(self.filename).read().split("\n")]
        self.D = [[float("inf") for _ in line] for line in self.data]
        self.D[0][0] = 0
        
    def part1(self):
        q = []
        visited = set() #(x, y, dir, consecutive_steps)
        visited.add((0, 0, None, 0))
        heapq.heappush(q, (0, Node(0, 0, 0, 0, None, 0))) #(dist, Node(x, y, w, dir, consecutive_steps))
        while q:
            dist, u = heapq.heappop(q)
            for dx, dy in directions4():
                
                if u.dir != None:
                    if (dx, dy) == (-u.dir[0], -u.dir[1]):
                        continue
                x, y = u.x + dx, u.y + dy
                if x < 0 or x >= len(self.data[0]) or y < 0 or y >= len(self.data):
                    continue
                
                consecutive_steps = 1
                if (dx, dy) == u.dir:
                    consecutive_steps = u.consecutive_steps + 1
                    
                if consecutive_steps > 3:
                    continue
                
                if (x, y, (dx, dy), consecutive_steps) in visited:
                    continue
                
                visited.add((x, y, (dx, dy), consecutive_steps))
                v = Node(x, y, self.data[y][x], float("inf"), (dx, dy), consecutive_steps)
                self.relax(u, v, v.w)
                
                if x == len(self.data[0]) - 1 and y == len(self.data) - 1:
                    return self.D[y][x]
                
                heapq.heappush(q, (v.d, v))
                
                
    def relax(self, u: Node, v: Node, w: int):
        if v.d > u.d + w:
            v.d = u.d + w
            self.D[v.y][v.x] = min(u.d + w, self.D[v.y][v.x])
            
    def specialRelax(self, u: Node, v: Node, dir):
        w = 0
        if dir == (0, 4):
            for i in range(u.y + 1, v.y + 1):
                w += self.data[i][v.x]
                
        elif dir == (0, -4):
            for i in range(u.y - 1, v.y - 1, -1):
                w += self.data[i][v.x]
                
        elif dir == (4, 0):
            for i in range(u.x + 1, v.x + 1):
                w += self.data[v.y][i]
                
        elif dir == (-4, 0):
            for i in range(u.x - 1, v.x - 1, -1):
                w += self.data[v.y][i]
                
        if v.d > u.d + w:
            v.d = u.d + w
            self.D[v.y][v.x] = min(u.d + w, self.D[v.y][v.x])
            
    def part2(self):
        self.D = [[float("inf") for _ in line] for line in self.data]
        self.D[0][0] = 0
        q = []
        visited = set() #(x, y, dir, consecutive_steps)
        visited.add((0, 0, None, 0))
        heapq.heappush(q, (0, Node(0, 0, 0, 0, None, 0))) #(dist, Node(x, y, w, dir, consecutive_steps))

        while q:
            dist, u = heapq.heappop(q)
            for dx, dy in directions4():
                
                if u.dir != None:
                    if (dx, dy) == (-u.dir[0], -u.dir[1]):
                        continue
                
                consecutive_steps = 4
                if (dx, dy) == u.dir:
                    consecutive_steps = u.consecutive_steps + 1
                else:
                    dx *= 4
                    dy *= 4   
                if consecutive_steps > 10:
                    continue
                
                x, y = u.x + dx, u.y + dy
                
                if x < 0 or x >= len(self.data[0]) or y < 0 or y >= len(self.data):
                    continue
                
                if (x, y, (dx, dy), consecutive_steps) in visited:
                    continue
                
                
                visited.add((x, y, (dx, dy), consecutive_steps))
                v = Node(x, y, self.data[y][x], float("inf"), (math.ceil(dx / 4), math.ceil(dy / 4)), consecutive_steps)
                
                if dx == 4 or dx == -4 or dy == 4 or dy == -4:
                    self.specialRelax(u, v, (dx, dy))
                else:
                    self.relax(u, v, v.w)
                
                heapq.heappush(q, (v.d, v))
                
        for line in self.D:
            print(line)
        return  self.D[len(self.data) - 1][len(self.data[0]) - 1]
    
    
    
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