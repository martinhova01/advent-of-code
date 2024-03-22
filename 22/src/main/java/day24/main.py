import math
import time
import itertools
from collections import Counter, defaultdict, deque
import networkx as nx
from tqdm import tqdm
import re
import copy

import sys
sys.path.append("../../../../..")
from utils import adjacent4, adjacent8, directions4, directions8

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [[[x] if x != "." else [] for x in line] for line in open(self.filename).read().strip().split("\n")]
        self.dirs = {">": (1, 0), "v": (0, 1), "<": (-1, 0), "^": (0, -1)}
        self.states = self.compute_states()
        
    def compute_states(self):
        n = math.lcm(len(self.data) - 2, len(self.data[0]) - 2)
        states = []
        for _  in range(n):
            states.append(self.data)
            self.move_blizzards()
        return states
            
            
    def move_blizzards(self):
        new_data = copy.deepcopy(self.data)
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                for c in self.data[y][x]:
                
                    if c == "#":
                        continue
                    
                    new_data[y][x].remove(c)
                    
                    dx, dy = self.dirs[c]
                    
                    if new_data[y + dy][x + dx] == ["#"]:
                        dx, dy = dx * 3, dy * 3
                        
                    new_data[(y + dy) % len(new_data)][(x + dx) % len(new_data[0])].append(c)
                    
        self.data = new_data
        
    def print_data(self):
        r = ""
        for line in self.data:
            for char_list in line:
                if len(char_list) == 0:
                    r += "."
                elif len(char_list) > 1:
                    r += str(len(char_list))
                else:
                    r += char_list[0]
            r += "\n"
        print(r)  
        
    def bfs(self, start, end, start_time):
        number_of_states = math.lcm(len(self.data) - 2, len(self.data[0]) - 2)
        visited = set() # (point, time)
        time = start_time
        q = deque()
        q.append((start, time)) # (point, time)
        while q:
            (x, y), t = q.popleft()
            
            if ((x, y), t % number_of_states) in visited:
                continue
            
            visited.add(((x, y), t % number_of_states))
            
            if time == t:
                time += 1
            
            if (x, y) == end:
                return t
            
                #try to go all 4 directions
            for (nx, ny) in adjacent4(x, y):
                if nx < 0 or ny < 0 or nx >= len(self.data[0]) or ny >= len(self.data):
                    continue
                
                if self.states[time % number_of_states][ny][nx] != []:
                    continue
                
                q.append(((nx, ny), time))
                
                #try to wait
            if self.states[time % number_of_states][y][x] != []:
                    continue
            
            q.append(((x, y), time))
                      
        
    def part1(self):
        start = (self.data[0].index([]), 0)
        end = (self.data[len(self.data) - 1].index([]), len(self.data) - 1)
        return self.bfs(start, end, 0)
    
    def part2(self):
        start = (self.data[0].index([]), 0)
        end = (self.data[len(self.data) - 1].index([]), len(self.data) - 1)
        
        t = self.bfs(start, end, 0)
        t = self.bfs(end, start, t)
        return self.bfs(start, end, t)
    
    
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