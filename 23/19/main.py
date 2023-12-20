from collections import deque
import time
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
            rules = re.split(r",|:", rules[:-1])
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
            statement= workflow[i]
            if ">" in statement:
                a, b = statement.split(">")
                a = part.atributes[a]
                b = int(b)
                i = i + 1 if a > b else i + 2
            else:
                a, b = statement.split("<")
                a = part.atributes[a]
                b = int(b)
                i = i + 1 if a < b else i + 2
        return workflow[i]
    
    
    def part1(self):
        s = 0
        for part in self.parts:
            if self.acceptsPart(part):
                s += sum(part.atributes.values())
        return s
    
    def findAcceptedPaths(self):
        
        startFlow = self.workflows["in"]
        paths = []
        q = deque()
        q.append((startFlow, 0, [startFlow[0]])) # (workflow, index_in_flow, visited)
        while q:
            flow, i, visited = q.popleft()
            
            if flow[i] == "R":
                continue
            if flow[i] == "A":
                paths.append(visited)
                continue
                
            if ">" not in flow[i] and "<" not in flow[i]:
                flow = self.workflows[flow[i]]
                statement = flow[0]
                next_visited = list(visited)
                next_visited.append(statement)
                q.append((flow, 0, next_visited))
                continue
                
            for b in (True, False):
                j = i + 1 if b else i + 2
                _next = flow[j]
                next_visited = list(visited)
                next_visited.append(b)
                if ">" in _next or "<" in _next: 
                    next_visited.append(_next)
                q.append((flow, j, next_visited))
        return paths
                
    def part2(self):
        paths = self.findAcceptedPaths()
        combs = 0
        
        for path in paths:
            acceptedRatings = {"x": set(range(1, 4001)), "m": set(range(1, 4001)), "a": set(range(1, 4001)), "s": set(range(1, 4001))}
            
            for i in range(len(path)):
                if path[i] == "A":
                    break
                if i % 2 == 0:
                    rating = path[i][0]
                    op = path[i][1]
                    num = int(path[i][2:])
                    if op == "<":
                        if path[i + 1]:
                                #remove >=
                            acceptedRatings[rating] = acceptedRatings[rating].difference(set(range(num, 4001)))
                                #remove <
                        else:
                            acceptedRatings[rating] = acceptedRatings[rating].difference(set(range(1, num)))
                    else:
                        if path[i + 1]:
                                #remove <=
                            acceptedRatings[rating] = acceptedRatings[rating].difference(set(range(1, num + 1)))
                        else:
                                #remove >
                            acceptedRatings[rating] = acceptedRatings[rating].difference(set(range(num + 1, 4001)))
                
            pathCombs = 1
            for val in acceptedRatings.values():
                pathCombs *= len(val)
                
            combs += pathCombs
        
        return combs

    
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