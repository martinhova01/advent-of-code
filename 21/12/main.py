import time
from collections import defaultdict, deque
class Solution():
    def __init__(self, test=False):
        self.test = test
        self.filename = "testinput.txt" if self.test else "input.txt"
        self.data = defaultdict(list)
        self.parse()
        
    def parse(self):
        for line in open(self.filename).read().split("\n"):
            data = line.split("-")
            start = data[0]
            end = data[1]
            self.data[start].append(end)
            self.data[end].append(start)
        
    def part1(self):
        paths = []
        q = deque()
        q.append(("start", {"start"}))
        while q:
            node, visited = q.popleft()
            for child in self.data[node]:
                if child == "end":
                    paths.append(visited)
                    continue
                if child.islower() and child in visited:
                    continue
                q.append((child, visited.union({child})))
                
        return len(paths)
                
    
    def part2(self):
        paths = []
        q = deque()
        q.append(("start", {"start"}, True))
        while q:
            node, visited, twoAvailable = q.popleft()
            for child in self.data[node]:
                two = twoAvailable
                if child == "end":
                    paths.append(visited)
                    continue
                if child == "start":
                    continue
                if child.islower() and child in visited and not twoAvailable:
                    continue
                if child.islower() and child in visited:
                    two = False
                q.append((child, visited.union({child}), two))
                
        return len(paths)
    
    
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