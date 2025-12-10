import time
import itertools
import functools
from collections import Counter, defaultdict, deque
import networkx as nx
from tqdm import tqdm
import numpy as np
import re
import copy
from functools import cache

import sys
sys.path.append("../..")
from utils import adjacent4, adjacent8, directions4, directions8, manhattanDist

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = [self.parse_line(line) for line in open(self.filename).read().rstrip().split("\n")]
        

    def parse_line(self, line):
        # Extract square-bracket string
        square = re.search(r"\[(.*?)\]", line).group(1)
        square = int(square.replace("#", "1").replace(".", "0")[::-1], 2)

        # Extract parenthesis groups as list of tuples
        parens = []
        for grp in re.findall(r"\((.*?)\)", line):
            nums = tuple(int(x) for x in grp.split(",")) if grp else ()
            num = int("".join(reversed(["1" if i in nums else "0" for i in range(max(nums) + 1)])), 2)
            parens.append(num)

        # Extract curly-bracket list of ints
        curly = [int(x) for x in re.search(r"\{(.*?)\}", line).group(1).split(",")]

        return square, parens, curly
    
    def get_num_presses(self, goal: int, buttons: list[int]) -> int:
        
        visited = set()
        q = deque([(0, 0)]) # indicator, clicks
        
        while q:
            
            indicators, clicks = q.popleft()
            # print(indicators, clicks)
            if indicators in visited:
                continue
            visited.add(indicators)
            
            if indicators == goal:
                return clicks
            
            for button in buttons:
                # print(indicators, button)
                next_indicators = indicators ^ button
                
                q.append((next_indicators, clicks + 1))
            
            
        
    def part1(self):
        s = 0
        for indicators, buttons, _ in self.data:
            print(indicators, buttons)
            s += self.get_num_presses(indicators, buttons)
        return s
    
    
    def get_num_presses_2(self, goal: int, buttons: list[int]) -> int:
        
        visited = set()
        q = deque([(0, 0)]) # indicator, clicks
        
        while q:
            
            indicators, clicks = q.popleft()
            # print(indicators, clicks)
            if indicators in visited:
                continue
            visited.add(indicators)
            
            if indicators == goal:
                return clicks
            
            for button in buttons:
                # print(indicators, button)
                next_indicators = indicators ^ button
                
                q.append((next_indicators, clicks + 1))
    
    def part2(self):
        s = 0
        for _, buttons, joltage in self.data:
            print(joltage, buttons)
            # s += self.get_num_presses(joltage, buttons)
        return s
    
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("---TEST---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}\n")
    
    # s = Solution()
    # print("---MAIN---")
    # print(f"part 1: {s.part1()}")
    # print(f"part 2: {s.part2()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()