import copy
import time
import itertools
from collections import Counter, defaultdict, deque
import networkx as nx
from tqdm import tqdm
import numpy as np
import re

import sys
sys.path.append("../..")
from utils import adjacent4, adjacent8, directions4, directions8

def is_number(s: str):
    return s.isdigit() or (s.startswith('-') and s[1:].isdigit())

class ALU():
    def __init__(self):
        self.registers = {"w": 0, "x": 0, "y": 0, "z": 0}
        
    def inp(self, a, value: int):
        self.registers[a] = value
        
    def add(self, a: str, b: str):
        if is_number(b):
            self.registers[a] = self.registers[a] + int(b)
        else:
            self.registers[a] = self.registers[a] + self.registers[b]
            
    def mul(self, a: str, b: str):
        if is_number(b):  
            self.registers[a] = self.registers[a] * int(b)
        else:
            self.registers[a] = self.registers[a] * self.registers[b]
            
    def div(self, a: str, b: str):
        if is_number(b):  
            if int(b) == 0:
                print("error: div by 0!!!")
                return
            self.registers[a] = int(self.registers[a] / int(b))
        else:
            self.registers[a] = int(self.registers[a] / self.registers[b])
            
    def mod(self, a: str, b: str):
        if is_number(b):
            if int(b) <= 0 or self.registers[a] < 0:
                print("error")  
            self.registers[a] = self.registers[a] % int(b)
        else:
            if self.registers[b] <= 0 or self.registers[a] < 0:
                print("error")  
            self.registers[a] = self.registers[a] % self.registers[b]
    
    def eql(self, a: str, b: str):
        if is_number(b):
            self.registers[a] = 1 if self.registers[a] == int(b) else 0
        else:
            self.registers[a] = 1 if self.registers[a] == self.registers[b] else 0
            
    def exec(self, program: list[str], input: list[int]) -> bool:
        self.input_counter = 0
        for instruction in program:
            if instruction.startswith("inp"):
                self.inp(instruction.split(" ")[1], input[self.input_counter])
                self.input_counter += 1
            elif instruction.startswith("add"):
                self.add(*instruction.split(" ")[1:])
            elif instruction.startswith("mul"):
                self.mul(*instruction.split(" ")[1:])
            elif instruction.startswith("div"):
                self.div(*instruction.split(" ")[1:])
            elif instruction.startswith("mod"):
                self.mod(*instruction.split(" ")[1:])
            elif instruction.startswith("eql"):
                self.eql(*instruction.split(" ")[1:])
        
    
    

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = None
        self.ALU = ALU()
        
    def part1(self):
        program = open(self.filename).read().split("\n")
        self.ALU.exec(program, [4, 3, 5, 7, 9, 2, 4, 6, 8, 9, 3, 9, 9, 1])
        print(self.ALU.registers)
        
                    
    
    def part2(self):
        return None
    
    
def main():
    start = time.perf_counter()
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()