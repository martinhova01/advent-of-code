import time
from tqdm import tqdm
import re

class Part:
    def __init__(self, x, m, a, s):
        self.atributes = {"x": x, "m": m, "a": a, "s": s}

class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.workflows = {}
        self.parts = []
        self.parse()
        
    def parse(self):
        workflows, parts = open(self.filename).read().split("\n\n")
        
        for line in workflows.split("\n"):
            label, rules = line.split("{")
            rules = rules[:-1].split(",")
            self.workflows[label] = rules
            
        for line in parts.split("\n"):
            vals = [int(x) for x in re.findall(r"\d+", line)]
            self.parts.append(Part(*vals))
            
    def acceptsPart(self, part):
        workflow = self.workflows["in"]
        
        while True:
            nextFlow = self.getNextFlow(workflow, part)
            if nextFlow == "A":
                return True
            elif nextFlow == "R":
                return False
            workflow = self.workflows[nextFlow]
            
            
    def getNextFlow(self, workflow, part):
        i = 0
        while ">" in workflow[i] or "<" in workflow[i]:
            statement, ifTrue = workflow[i].split(":")
            if ">" in statement:
                a, b = statement.split(">")
                a = part.atributes[a]
                b = int(b)
                if a > b:
                    return ifTrue
                else:
                    i += 1
            else:
                a, b = statement.split("<")
                a = part.atributes[a]
                b = int(b)
                if a < b:
                    return ifTrue
                else:
                    i += 1
        return workflow[i]
            
        
    def part1(self):
        s = 0
        for part in self.parts:
            if self.acceptsPart(part):
                s += sum(part.atributes.values())
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
    print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}")
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()