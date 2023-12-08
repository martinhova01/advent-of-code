import math
import time
import re

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.instructions = ""
        self.data = {}
        self.parse()
        
    def parse(self):
        sections = open(self.filename).read().split("\n\n")
        self.instructions = sections[0]
        for line in sections[1].split("\n"):
            nodes = re.findall(r"\w+", line)
            self.data[nodes[0]] = (nodes[1], nodes[2])
        
        
    def part1(self):
        return self.distToNextEndNode("AAA")
    
    def distToNextEndNode(self, node):
        i = 0
        c = 0
        first = True
        while not node.endswith("Z") or first:
            first = False
            if self.instructions[i] == "L":
                node = self.data[node][0]
            else:
                node = self.data[node][1]
            i = (i + 1) % len(self.instructions)
            c += 1
        return c
    
    def part2(self):
        dist = []
        for startNode in self.data.keys():
            if startNode.endswith("A"):
                dist.append(self.distToNextEndNode(startNode))     
        return math.lcm(*dist)
             
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("---TEST---")
    # print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}\n")
    
    s = Solution()
    print("---MAIN---")
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()