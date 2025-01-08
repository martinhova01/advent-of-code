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
        self.data = open(self.filename).read().rstrip().split("\n")
        self.numbers = {
            "7": (0, 0),
            "8": (1, 0),
            "9": (2, 0),
            "4": (0, 1),
            "5": (1, 1),
            "6": (2, 1),
            "1": (0, 2),
            "2": (1, 2),
            "3": (2, 2),
            "0": (1, 3),
            "A": (2, 3)
        }
        self.directions = {
            "^": (1, 0),
            "A": (2, 0),
            "<": (0, 1),
            "v": (1, 1),
            ">": (2, 1)
        }
        
    def find_sequence(self, target: str):
        sequences = [""]
        x, y, = None, None
        if target[:-1].isnumeric():
            x, y = 2, 3
            for c in target:
                goal = self.numbers[c]
                dx, dy = goal[0] - x, goal[1] - y
                addition_x = ""
                if dx < 0:
                    addition_x = "<" * abs(dx)
                else:
                    addition_x = ">" * dx
                
                addition_y = ""
                if dy < 0:
                    addition_y = "^" * abs(dy)
                else:
                    addition_y = "v" * dy
                    
                if x == 0 and goal[1] == 3:
                    new_sequences = []
                    for seq in sequences:
                        new_sequences.append(seq + addition_x + addition_y + "A")
                    sequences = new_sequences
                
                elif y == 3 and goal[0] == 0:
                    new_sequences = []
                    for seq in sequences:
                        new_sequences.append(seq + addition_y + addition_x + "A")
                    sequences = new_sequences
                
                else:
                    new_sequences = []
                    for seq in sequences:
                        new_sequences.append(seq + addition_x + addition_y + "A")
                        new_sequences.append(seq + addition_y + addition_x + "A")
                    sequences = new_sequences
                x, y = goal
                      
        else:
            x, y = 2, 0
            for c in target:
                goal = self.directions[c]
                dx, dy = goal[0] - x, goal[1] - y
                addition_x = ""
                if dx < 0:
                    addition_x = "<" * abs(dx)
                else:
                    addition_x = ">" * dx
                
                addition_y = ""
                if dy < 0:
                    addition_y = "^" * abs(dy)
                else:
                    addition_y = "v" * dy
                    
                if x == 0 and y == 1:
                    new_sequences = []
                    for seq in sequences:
                        new_sequences.append(seq + addition_x + addition_y + "A")
                    sequences = new_sequences
                
                elif y == 0 and goal[0] == 0:
                    new_sequences = []
                    for seq in sequences:
                        new_sequences.append(seq + addition_y + addition_x + "A")
                    sequences = new_sequences
                
                else:
                    new_sequences = []
                    for seq in sequences:
                        new_sequences.append(seq + addition_x + addition_y + "A")
                        new_sequences.append(seq + addition_y + addition_x + "A")
                    sequences = new_sequences
                x, y = goal
        
        return min(sequences, key=len)
            
        
        
                
    def part1(self):
        s = 0
        for i in range(len(self.data)):
            sequence = self.data[i]
            for _ in range(3):
                sequence = self.find_sequence(sequence)
            
            print(sequence, len(sequence), int(self.data[i][:-1]))
            
            s += len(sequence) * int(self.data[i][:-1])

        return s
        
    
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
    print(f"part 1: {s.part1()}") # 131526 too high
    print(f"part 2: {s.part2()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()