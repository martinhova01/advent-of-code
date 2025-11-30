import time
import itertools
import functools
from collections import Counter, defaultdict, deque
import networkx as nx
from tqdm import tqdm
import numpy as np
import re
import copy

import sys
sys.path.append("../..")
from utils import adjacent4, adjacent8, directions4, directions8, manhattanDist

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = open(self.filename).read().rstrip()
        self.operators = {"AND", "LSHIFT", "NOT", "OR", "RSHIFT", "NOP"}
        
    def simulate(self, wire):
        instruction = self.G[wire]
        value = None 
        if instruction[3]:
            print(instruction[3])
            return instruction[3]
        
        operation = instruction[0]
        if operation == "NOP":
            value = self.simulate(instruction[2][0])
        elif operation == "NOT":
            value = (~self.simulate(instruction[2][0])) % 65536
        elif operation == "LSHIFT":
            value = (self.simulate(instruction[2][0]) * (2**instruction[1])) % 65536
        elif operation == "RSHIFT":
            value = (self.simulate(instruction[2][0]) // 2**(instruction[1])) % 65536
        elif operation == "OR":
            value = (self.simulate(instruction[2][0]) | self.simulate(instruction[2][1])) % 65536
        elif operation == "AND":
            value = (self.simulate(instruction[2][0]) & self.simulate(instruction[2][1])) % 65536
        # print(value)
        return value
            
        
        
    def part1(self):
        self.G = {}  # id: [operator, amount, [children], value]
        for line in self.data.split("\n"):
            operation, wire = line.split(" -> ")
            if not any(op in operation for op in self.operators):
                if operation.isdigit():
                    self.G[wire] = [None, None, None, int(operation)]
                else:
                    self.G[wire] = ["NOP", None, [operation], None]
            else:
                children = re.findall(r"\b[a-z]+\b", operation)
                operator = re.findall("|".join(self.operators), operation)[0]
                if operator in ["RSHIFT", "LSHIFT"]:
                    amount = re.findall(r"\d+", operation)[0]
                    self.G[wire] = [operator, int(amount), children, None]
                else: 
                    self.G[wire] = [operator, None, children, None]
        
        return self.simulate("a")
        #problem line: 1 AND ht -> hu
        
        
    
    def part2(self):
        return None
    
    
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