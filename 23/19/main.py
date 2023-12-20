from collections import deque
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
        self.mapping = {}
        self.parse()
        self.createMap()
        print(self.mapping)
        
    def createMap(self):
        for workflow in self.workflows.values():
            for i in range(len(workflow)):
                if ">" in workflow[i] or "<" in workflow[i]:
                    statement = workflow[i]
                    isTrue = workflow[i + 1]
                    if ">" not in isTrue and "<" not in isTrue and isTrue != "A" and isTrue != "R":
                        isTrue = self.workflows[isTrue][0]
                    isFalse = workflow[i + 2]
                    if ">" not in isFalse and "<" not in isFalse and isFalse != "A" and isFalse != "R":
                        isFalse = self.workflows[isFalse][0]
                    self.mapping[statement] = (isTrue, isFalse)
        
    def parse(self):
        workflows, parts = open(self.filename).read().split("\n\n")
        
        for line in workflows.split("\n"):
            label, rules = line.split("{")
            # rules = rules[:-1].split(",")
            rules = re.split(r",|:", rules[:-1])
            self.workflows[label] = rules
            
        for line in parts.split("\n"):
            vals = [int(x) for x in re.findall(r"\d+", line)]
            self.parts.append(Part(*vals))
            
    # def acceptsPart(self, part):
    #     workflow = self.workflows["in"]
        
    #     while True:
    #         nextFlow = self.getNextFlow(workflow, part)
    #         if nextFlow == "A":
    #             return True
    #         elif nextFlow == "R":
    #             return False
    #         workflow = self.workflows[nextFlow]
            
            
    # def getNextFlow(self, workflow, part):
    #     i = 0
    #     while ">" in workflow[i] or "<" in workflow[i]:
    #         statement, ifTrue = workflow[i].split(":")
    #         if ">" in statement:
    #             a, b = statement.split(">")
    #             a = part.atributes[a]
    #             b = int(b)
    #             if a > b:
    #                 return ifTrue
    #             else:
    #                 i += 1
    #         else:
    #             a, b = statement.split("<")
    #             a = part.atributes[a]
    #             b = int(b)
    #             if a < b:
    #                 return ifTrue
    #             else:
    #                 i += 1
    #     return workflow[i]
    
    def findRejectedPaths(self):
        paths = []
        q = deque()
        firstStatement = self.workflows["in"][0]
        q.append((firstStatement, [firstStatement]))
        while q:
            statement, visited = q.popleft()
            if statement == "R":
                paths.append(visited)
                continue
            if statement == "A":
                continue
            
            v = list(visited)
            v.append(True)
            isTrue = self.mapping[statement][0]
            v.append(isTrue)
            q.append((isTrue, v))
            
            v = list(visited)
            v.append(False)
            isFalse = self.mapping[statement][1]
            v.append(isFalse)
            q.append((isFalse, v))
        
        return paths
            
            
        
    # def part1(self):
    #     s = 0
    #     for part in self.parts:
    #         if self.acceptsPart(part):
    #             s += sum(part.atributes.values())
    #     return s
    
    def part2(self):
        paths = self.findRejectedPaths()
        # print(paths)
        # print(len(paths))
        combs = 4000**4
        # self.acceptedRatings = {"x": set(), "m": set(), "a": set(), "s": set()}
        
        for path in paths:
            rejectedRatings = {"x": set(range(1, 4001)), "m": set(range(1, 4001)), "a": set(range(1, 4001)), "s": set(range(1, 4001))}
            
            for i in range(len(path)):
                if path[i] == "R":
                    break
                if i % 2 == 0:
                    rating = path[i][0]
                    op = path[i][1]
                    num = int(path[i][2:])
                    if op == "<":
                        if path[i + 1]:
                                #remove >=
                            rejectedRatings[rating] = rejectedRatings[rating].difference(set(range(num, 4001)))
                                #remove <
                        else:
                            rejectedRatings[rating] = rejectedRatings[rating].difference(set(range(1, num)))
                    else:
                        if path[i + 1]:
                                #remove <=
                            rejectedRatings[rating] = rejectedRatings[rating].difference(set(range(1, num + 1)))
                        else:
                                #remove >
                            rejectedRatings[rating] = rejectedRatings[rating].difference(set(range(num + 1, 4001)))
                
            pathCombs = 1
            for val in rejectedRatings.values():
                pathCombs *= len(val)
                
            # print(pathCombs)
            combs -= pathCombs
            
            
        return combs
        
    
    
def main():
    start = time.perf_counter()
    
    s = Solution(test=True)
    print("---TEST---")
    # print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}\n")
    
    s = Solution()
    print("---MAIN---")
    # # print(f"part 1: {s.part1()}")
    print(f"part 2: {s.part2()}") # 150916513783634 - too high
    
    print(f"\nTotal time: {time.perf_counter() - start : .4f} sec")
    
main()